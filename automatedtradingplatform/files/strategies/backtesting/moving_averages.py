#!/usr/bin/python

from __future__ import print_function
from pyalgotrade import strategy
from pyalgotrade.technical import ma
from pyalgotrade.technical import cross
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.stratanalyzer import returns
from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import drawdown
from pyalgotrade.stratanalyzer import trades
import argparse
import sys

# Nagios constants
OK          = 0
WARNING     = 1
CRITICAL    = 2
UNKNOWN     = 3

class MovingAverages(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument, shortSmaPeriod, longSmaPeriod):
        super(MovingAverages, self).__init__(feed)
        self.__instrument = instrument
        self.__position = None
        # We'll use adjusted close values instead of regular close values.
        self.setUseAdjustedValues(True)
        self.__prices = feed[instrument].getPriceDataSeries()
        self.__shortSma = ma.SMA(self.__prices, shortSmaPeriod)
        self.__longSma = ma.SMA(self.__prices, longSmaPeriod)

    def getSMA(self):
        return self.__sma

    def onEnterCanceled(self, position):
        self.__position = None

    def onExitOk(self, position):
        self.__position = None

    def onExitCanceled(self, position):
        # If the exit was canceled, re-submit it.
        self.__position.exitMarket()

    def onBars(self, bars):  
        # Wait for enough bars to be available to calculate a SMA.
        if self.__shortSma[-1] is None and self.__longSma is None:
            return

        bar = bars[self.__instrument]

        # If a position was not opened, check if we should enter a long position.
        if self.__position is None:
            if self.__shortSma[-1] > self.__longSma[-1]:

                shares = int(self.getBroker().getCash() * 0.9 / bars[self.__instrument].getPrice())
                self.__position = self.enterLong(self.__instrument, shares, True)

                # Check if we have to exit the position.
        elif  self.__shortSma[-1] < self.__longSma[-1] and not self.__position.exitActive():
            self.__position.exitMarket()


cmd_arg_help = "Backtest to accompany the moving averages strategy"

if __name__=="__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker of the stock to run the strategy against")

    args = parser.parse_args()

    if not args.ticker:
        print("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    instrument = args.ticker
    shortSmaPeriod = 10
    longSmaPeriod = 50

    # Load the bars. This file was manually downloaded from Yahoo Finance.
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV(instrument, "/atp/ticker-data/"+instrument+".AX.txt")

    myStrategy = MovingAverages(feed, instrument, shortSmaPeriod, longSmaPeriod)

    # Attach different analyzers to a strategy before executing it.
    retAnalyzer = returns.Returns()
    myStrategy.attachAnalyzer(retAnalyzer)
    sharpeRatioAnalyzer = sharpe.SharpeRatio()
    myStrategy.attachAnalyzer(sharpeRatioAnalyzer)
    drawDownAnalyzer = drawdown.DrawDown()
    myStrategy.attachAnalyzer(drawDownAnalyzer)
    tradesAnalyzer = trades.Trades()
    myStrategy.attachAnalyzer(tradesAnalyzer)

    # Run the strategy.
    myStrategy.run()

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
