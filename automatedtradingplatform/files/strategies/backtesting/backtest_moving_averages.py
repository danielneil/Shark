#!/usr/bin/python3

from __future__ import print_function

from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.technical import ma
from pyalgotrade.stratanalyzer import sharpe

import argparse
import sys

# Nagios constants. 

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "Example Backtest: trigger a buy when the shorter simple moving average, crosses above the longer simple moving average"

strategy_name = "Moving Averages Backtest"

class MovingAverages(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument, shares, capital, longsma, shortsma):
        super(MovingAverages, self).__init__(feed, capital)
        self.__position = None
        self.__instrument = instrument
        # We'll use adjusted close values instead of regular close values.
        self.setUseAdjustedValues(True)
        self.__longSma = ma.SMA(feed[instrument].getPriceDataSeries(), longsma)
        self.__shortSma = ma.SMA(feed[instrument].getPriceDataSeries(), shortsma)

    def onEnterOk(self, position):
        execInfo = position.getEntryOrder().getExecutionInfo()

    def onEnterCanceled(self, position):
        self.__position = None

    def onExitOk(self, position):
        execInfo = position.getExitOrder().getExecutionInfo()
        self.__position = None

    def onExitCanceled(self, position):
        # If the exit was canceled, re-submit it.
        self.__position.exitMarket()

    def onBars(self, bars):
        # Wait for enough bars to be available to calculate a SMA.
        if self.__longSma[-1] is None:
            return

        if self.__shortSma[-1] is None:
            return

        bar = bars[self.__instrument]
        # If a position was not opened, check if we should enter a long position.
        if self.__position is None:
            if self.__shortSma[-1] > self.__longSma[-1]:
                # Enter a buy market order for n shares. The order is good till canceled.
                self.__position = self.enterLong(self.__instrument, shares, True)
        # Check if we have to exit the position.
        elif self.__shortSma[-1] < self.__longSma[-1] and not self.__position.exitActive():
            self.__position.exitMarket()


def run_strategy(ticker, shares, capital, longsma, shortsma):
    # Load the bar feed from the CSV file
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV(ticker, "/shark/ticker-data/"+ticker+".AX.txt")

    # Evaluate the strategy with the feed.
    strat = MovingAverages(feed, ticker, shares, capital, longsma, shortsma)
    
    # Attach  analyzers to the strategy before executing it.
    sharpeRatioAnalyzer = sharpe.SharpeRatio()
    strat.attachAnalyzer(sharpeRatioAnalyzer)
    
    retAnalyzer = returns.Returns()
    strat.attachAnalyzer(retAnalyzer)
    
    drawDownAnalyzer = drawdown.DrawDown()
    strat.attachAnalyzer(drawDownAnalyzer)
    
    tradesAnalyzer = trades.Trades()
    strat.attachAnalyzer(tradesAnalyzer)

    strat.run()
    
    
    
    
    print("Final portfolio value: $%.2f" % myStrategy.getResult())
    print("Cumulative returns: %.2f %%" % (retAnalyzer.getCumulativeReturns()[-1] * 100))
    print("Sharpe ratio: %.2f" % (sharpeRatioAnalyzer.getSharpeRatio(0.05)))
    print("Max. drawdown: %.2f %%" % (drawDownAnalyzer.getMaxDrawDown() * 100))
    print("Longest drawdown duration: %s" % (drawDownAnalyzer.getLongestDrawDownDuration()))

    print("")
    print("Total trades: %d" % (tradesAnalyzer.getCount()))

    if tradesAnalyzer.getCount() > 0:
      profits = tradesAnalyzer.getAll()
      print("Avg. profit: $%2.f" % (profits.mean()))
      print("Profits std. dev.: $%2.f" % (profits.std()))
      print("Max. profit: $%2.f" % (profits.max()))
      print("Min. profit: $%2.f" % (profits.min()))
      returns = tradesAnalyzer.getAllReturns()
      print("Avg. return: %2.f %%" % (returns.mean() * 100))
      print("Returns std. dev.: %2.f %%" % (returns.std() * 100))
      print("Max. return: %2.f %%" % (returns.max() * 100))
      print("Min. return: %2.f %%" % (returns.min() * 100)) 

      print("")
      print("Profitable trades: %d" % (tradesAnalyzer.getProfitableCount()))

   if tradesAnalyzer.getProfitableCount() > 0:
      profits = tradesAnalyzer.getProfits()
      print("Avg. profit: $%2.f" % (profits.mean()))
      print("Profits std. dev.: $%2.f" % (profits.std()))
      print("Max. profit: $%2.f" % (profits.max()))
      print("Min. profit: $%2.f" % (profits.min()))
      returns = tradesAnalyzer.getPositiveReturns()
      print("Avg. return: %2.f %%" % (returns.mean() * 100))
      print("Returns std. dev.: %2.f %%" % (returns.std() * 100))
      print("Max. return: %2.f %%" % (returns.max() * 100))
      print("Min. return: %2.f %%" % (returns.min() * 100))

      print("")
      print("Unprofitable trades: %d" % (tradesAnalyzer.getUnprofitableCount()))

   if tradesAnalyzer.getUnprofitableCount() > 0:
     losses = tradesAnalyzer.getLosses()
     print("Avg. loss: $%2.f" % (losses.mean()))
     print("Losses std. dev.: $%2.f" % (losses.std()))
     print("Max. loss: $%2.f" % (losses.min()))
     print("Min. loss: $%2.f" % (losses.max()))
     returns = tradesAnalyzer.getNegativeReturns()
     print("Avg. return: %2.f %%" % (returns.mean() * 100))
     print("Returns std. dev.: %2.f %%" % (returns.std() * 100))
     print("Max. return: %2.f %%" % (returns.max() * 100))
     print("Min. return: %2.f %%" % (returns.min() * 100))
    
    
    
    
   print("Sharpe Ratio: %.2f" % sharpeRatioAnalyzer.getSharpeRatio(0.05))
   sharpeRatio = sharpeRatioAnalyzer.getSharpeRatio(0.05)

    # Write detailed backtest file to the web dir


   if sharpeRatio > 0: 
       sys.exit(OK)
   else:
       sys.exit(CRITICAL)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker of the stock to run the backtest against.")
    parser.add_argument("-s", "--shares", help="The number of imaginary shares to purchase.")
    parser.add_argument("-c", "--capital", help="The imaginary amount of capital available (in dollars).")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    if not args.shares:
        print("UNKNOWN - No shares specified")
        sys.exit(UNKNOWN)

    if not args.capital:
        print("UNKNOWN - No capital amount specified")
        sys.exit(UNKNOWN)

    ticker = args.ticker 
    shares = int(args.shares)
    capital = int(args.capital)

    longer_sma = 50
    shorter_sma = 10
    
    run_strategy(ticker, shares, capital, longer_sma, shorter_sma)
