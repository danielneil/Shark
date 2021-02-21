#!/usr/bin/python3

from __future__ import print_function

from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.technical import ma

from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import drawdown
from pyalgotrade.stratanalyzer import trades
import pyalgotrade

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
    retAnalyzer = pyalgotrade.stratanalyzer.returns.Returns()
    strat.attachAnalyzer(retAnalyzer)

    sharpeRatioAnalyzer = sharpe.SharpeRatio()
    strat.attachAnalyzer(sharpeRatioAnalyzer)
    sharpeRatio = 0
   
    drawDownAnalyzer = drawdown.DrawDown()
    strat.attachAnalyzer(drawDownAnalyzer)
    
    tradesAnalyzer = trades.Trades()
    strat.attachAnalyzer(tradesAnalyzer)

    strat.run()

    with open("/shark/backtest/" + ticker + ".html", 'w') as htmlFile:

        htmlFile.write("Final portfolio value: $%.2f" % strat.getResult())
        htmlFile.write("Cumulative returns: %.2f %%" % (retAnalyzer.getCumulativeReturns()[-1] * 100))

        sharpeRatio = sharpeRatioAnalyzer.getSharpeRatio(0.05)

        htmlFile.write("Sharpe ratio: %.2f" % (sharpeRatio))
        htmlFile.write("Max. drawdown: %.2f %%" % (drawDownAnalyzer.getMaxDrawDown() * 100))
        htmlFile.write("Longest drawdown duration: %s" % (drawDownAnalyzer.getLongestDrawDownDuration()))

        htmlFile.write("")
        htmlFile.write("Total trades: %d" % (tradesAnalyzer.getCount()))

        if tradesAnalyzer.getCount() > 0:

            profits = tradesAnalyzer.getAll()

            htmlFile.write("Avg. profit: $%2.f" % (profits.mean()))
            htmlFile.write("Profits std. dev.: $%2.f" % (profits.std()))
            htmlFile.write("Max. profit: $%2.f" % (profits.max()))
            htmlFile.write("Min. profit: $%2.f" % (profits.min()))

            returns = tradesAnalyzer.getAllReturns()

            htmlFile.write("Avg. return: %2.f %%" % (returns.mean() * 100))
            htmlFile.write("Returns std. dev.: %2.f %%" % (returns.std() * 100))
            htmlFile.write("Max. return: %2.f %%" % (returns.max() * 100))
            htmlFile.write("Min. return: %2.f %%" % (returns.min() * 100)) 

            htmlFile.write("")
            htmlFile.write("Profitable trades: %d" % (tradesAnalyzer.getProfitableCount()))

        if tradesAnalyzer.getProfitableCount() > 0:

            profits = tradesAnalyzer.getProfits()

            htmlFile.write("Avg. profit: $%2.f" % (profits.mean()))
            htmlFile.write("Profits std. dev.: $%2.f" % (profits.std()))
            htmlFile.write("Max. profit: $%2.f" % (profits.max()))
            htmlFile.write("Min. profit: $%2.f" % (profits.min()))

            returns = tradesAnalyzer.getPositiveReturns()

            htmlFile.write("Avg. return: %2.f %%" % (returns.mean() * 100))
            htmlFile.write("Returns std. dev.: %2.f %%" % (returns.std() * 100))
            htmlFile.write("Max. return: %2.f %%" % (returns.max() * 100))
            htmlFile.write("Min. return: %2.f %%" % (returns.min() * 100))

            htmlFile.write("")
            htmlFile.write("Unprofitable trades: %d" % (tradesAnalyzer.getUnprofitableCount()))

        if tradesAnalyzer.getUnprofitableCount() > 0:

            losses = tradesAnalyzer.getLosses()

            htmlFile.write("Avg. loss: $%2.f" % (losses.mean()))
            htmlFile.write("Losses std. dev.: $%2.f" % (losses.std()))
            htmlFile.write("Max. loss: $%2.f" % (losses.min()))
            htmlFile.write("Min. loss: $%2.f" % (losses.max()))

            returns = tradesAnalyzer.getNegativeReturns()

            htmlFile.write("Avg. return: %2.f %%" % (returns.mean() * 100))
            htmlFile.write("Returns std. dev.: %2.f %%" % (returns.std() * 100))
            htmlFile.write("Max. return: %2.f %%" % (returns.max() * 100))
            htmlFile.write("Min. return: %2.f %%" % (returns.min() * 100))
    
            htmlFile.write("Sharpe Ratio: %.2f" % sharpeRatioAnalyzer.getSharpeRatio(0.05))


    print("Sharpe Ratio: %.2f" % sharpeRatioAnalyzer.getSharpeRatio(0.05))


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
