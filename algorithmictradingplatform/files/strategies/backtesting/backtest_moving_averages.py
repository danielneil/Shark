#!/usr/bin/python3

from __future__ import print_function

from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed

from pyalgotrade.technical import ma
from pyalgotrade.technical import cross

from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import drawdown
from pyalgotrade.stratanalyzer import trades
from pyalgotrade import plotter
import pyalgotrade

import argparse
import sys
import os

import time

from backtest_functions import CreateHTMLReport
from backtest_functions import CreateJSONTransactionLog
from backtest_functions import CreateJSONTransactionLogHTML

# Nagios constants. 

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "Example Backtest: Buy when a moving average cross above occurs, sell when a cross below happens."
strategy_name = "Moving Averages Crossover Backtest"

class MovingAverages(strategy.BacktestingStrategy):

    def __init__(self, feed, instrument, shares, capital, smaPeriod, tradeLog):

        super(MovingAverages, self).__init__(feed, capital)

        self.__position = None
        self.__instrument = instrument
        self.__prices = feed[instrument].getPriceDataSeries()

        self.__tradeLog = tradeLog

        # We'll use adjusted close values instead of regular close values.
        self.setUseAdjustedValues(True)

        self.__sma = ma.SMA(self.__prices, smaPeriod)

    def onEnterOk(self, position):

        execInfo = position.getEntryOrder().getExecutionInfo()
        quantity = str(execInfo.getQuantity())

        tradeLogDict = {
                    "datetime": str(execInfo.getDateTime()),
                    "action": "BUY",
                    "ticker": ticker,
                    "quantity": quantity,
                    "price": execInfo.getPrice()
                }

        self.__tradeLog.append(tradeLogDict)

    def onEnterCanceled(self, position):
        self.__position = None

    def onExitOk(self, position):

        execInfo = position.getExitOrder().getExecutionInfo()
        quantity = str(execInfo.getQuantity())

        tradeLogDict = {
                    "datetime": str(execInfo.getDateTime()),
                    "action": "SELL",
                    "ticker": ticker,
                    "quantity": quantity, 
                    "price": execInfo.getPrice()
                }

        self.__tradeLog.append(tradeLogDict)

        self.__position = None

    def onExitCanceled(self, position):
        # If the exit was canceled, re-submit it.
        self.__position.exitMarket()

    def onBars(self, bars):
        # If a position was not opened, check if we should enter a long position.
        if self.__position is None:

            if cross.cross_above(self.__prices, self.__sma) > 0:

                # Enter a buy market order for n shares. The order is good till canceled.
                self.__position = self.enterLong(self.__instrument, shares, True)

        # Check if we have to exit the position.
        elif cross.cross_below(self.__prices, self.__sma) > 0 and not self.__position.exitActive():
            self.__position.exitMarket()


def run_strategy(ticker, shares, capital, smaPeriod, generate_reports):

    # Measure the execution time of the backtest.
    start_time = time.time()

    # Load the bar feed from the CSV file
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV(ticker, "/shark/ticker-data/"+ticker+".AX.txt")

    # Create a dict to store the trade log.
    tradeLog = []

    # Evaluate the strategy with the feed.
    strat = MovingAverages(feed, ticker, shares, capital, smaPeriod, tradeLog)
    
    # Attach  analyzers to the strategy before executing it.
    retAnalyzer = pyalgotrade.stratanalyzer.returns.Returns()
    strat.attachAnalyzer(retAnalyzer)

    sharpeRatioAnalyzer = sharpe.SharpeRatio()
    strat.attachAnalyzer(sharpeRatioAnalyzer)
   
    drawDownAnalyzer = drawdown.DrawDown()
    strat.attachAnalyzer(drawDownAnalyzer)
    
    tradesAnalyzer = trades.Trades()
    strat.attachAnalyzer(tradesAnalyzer)

    # Attach the plotter
    plot = plotter.StrategyPlotter(strat)

    strat.run()
    
    if generate_reports:
        
        # Save the plot.
        plot.savePlot("/shark/backtest/html/" + ticker + ".png") 

        # measure the execution time to here.
        time_taken = ( time.time() - start_time )

        # Generate the HTML Report    
        CreateHTMLReport(ticker, strat, retAnalyzer, sharpeRatioAnalyzer, drawDownAnalyzer, tradesAnalyzer, time_taken)

        # Generate the trade log json file.
        CreateJSONTransactionLog(tradeLog, ticker)
    
        # Generate the trade log in HTML
        CreateJSONTransactionLogHTML(ticker)

    print("Sharpe Ratio: %.2f" % sharpeRatioAnalyzer.getSharpeRatio(0.05))

    if sharpeRatioAnalyzer.getSharpeRatio(0.05) > 0: 
       sys.exit(OK)
    else:
       sys.exit(CRITICAL)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker of the stock to run the backtest against.")
    parser.add_argument("-s", "--shares", help="The number of imaginary shares to purchase.")
    parser.add_argument("-c", "--capital", help="The imaginary amount of capital available (in dollars).")
    parser.add_argument("-n", "--noreport", help="Do not generate the back test report", action="store_true", default=False)
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
    
    smaPeriod = 50

    run_strategy(ticker, shares, capital, smaPeriod, args.noreport)
