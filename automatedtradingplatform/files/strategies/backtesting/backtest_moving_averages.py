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
    def __init__(self, feed, instrument, smaPeriod, shares, capital):
        super(MovingAverages, self).__init__(feed, capital)
        self.__position = None
        self.__instrument = instrument
        # We'll use adjusted close values instead of regular close values.
        self.setUseAdjustedValues(True)
        self.__sma = ma.SMA(feed[instrument].getPriceDataSeries(), smaPeriod)

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
        if self.__sma[-1] is None:
            return

        bar = bars[self.__instrument]
        # If a position was not opened, check if we should enter a long position.
        if self.__position is None:
            if bar.getPrice() > self.__sma[-1]:
                # Enter a buy market order for 10 shares. The order is good till canceled.
                self.__position = self.enterLong(self.__instrument, shares, True)
        # Check if we have to exit the position.
        elif bar.getPrice() < self.__sma[-1] and not self.__position.exitActive():
            self.__position.exitMarket()


def run_strategy(smaPeriod, ticker, shares, capital):
    # Load the bar feed from the CSV file
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV(ticker, "/atp/ticker-data/"+ticker+".AX.txt")

    # Evaluate the strategy with the feed.
    maStrategy = MovingAverages(feed, ticker, smaPeriod, shares, capital)
    
    sharpeRatioAnalyzer = sharpe.SharpeRatio()
    maStrategy.attachAnalyzer(sharpeRatioAnalyzer)
    
    maStrategy.run()
    
    # print("Final portfolio value: $%.2f" % maStrategy.getBroker().getEquity())
    
    print("Sharpe Ratio: %.2f" % sharpeRatioAnalyzer.getSharpeRatio(0.05))

    sharpeRatio = sharpeRatioAnalyzer.getSharpeRatio(0.05)

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
    
    run_strategy(15, ticker, shares, capital)
