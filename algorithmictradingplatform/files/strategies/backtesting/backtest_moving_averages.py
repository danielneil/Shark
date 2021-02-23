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

# Nagios constants. 

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "Example Backtest: Buy when a moving average cross above occurs, sell when a cross below happens."
strategy_name = "Moving Averages Crossover Backtest"

class MovingAverages(strategy.BacktestingStrategy):

    def __init__(self, feed, instrument, shares, capital, smaPeriod):

        super(MovingAverages, self).__init__(feed, capital)

        self.__position = None
        self.__instrument = instrument
        self.__prices = feed[instrument].getPriceDataSeries()

        # We'll use adjusted close values instead of regular close values.
        self.setUseAdjustedValues(True)

        self.__sma = ma.SMA(self.__prices, smaPeriod)

        # if our trade log exists, delete it.
        if os.path.isfile("/shark/backtest/" + ticker + ".trade.log"):
            os.remove("/shark/backtest/" + ticker + ".trade.log")

    def onEnterOk(self, position):

        execInfo = position.getEntryOrder().getExecutionInfo()
        quantity = str(execInfo.getQuantity())

        with open("/shark/backtest/" + ticker + ".trade.log", "a") as tradeLog:
            tradeLog.write(str(execInfo.getDateTime()) + ": BUY "+ticker+" ("+quantity+" shares) at $%.2f" % (execInfo.getPrice()) + ")\n")

    def onEnterCanceled(self, position):
        self.__position = None

    def onExitOk(self, position):
        execInfo = position.getExitOrder().getExecutionInfo()
        self.__position = None

        execInfo = position.getEntryOrder().getExecutionInfo()
        quantity = str(execInfo.getQuantity())

        with open("/shark/backtest/" + ticker + ".trade.log", "a") as tradeLog:
            tradeLog.write(str(execInfo.getDateTime()) + ": SELL "+ticker+" ("+quantity+" shares) at $%.2f" % (execInfo.getPrice()) + ")\n")

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

            if cross.cross_above(self.__prices, self.__sma) > 0:

                # Enter a buy market order for n shares. The order is good till canceled.
                self.__position = self.enterLong(self.__instrument, shares, True)

        # Check if we have to exit the position.
        elif cross.cross_below(self.__prices, self.__sma) > 0 and not self.__position.exitActive():
            self.__position.exitMarket()


def run_strategy(ticker, shares, capital, smaPeriod):

    # Load the bar feed from the CSV file
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV(ticker, "/shark/ticker-data/"+ticker+".AX.txt")

    # Evaluate the strategy with the feed.
    strat = MovingAverages(feed, ticker, shares, capital, smaPeriod)
    
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

    # Attach the plotter
    plot = plotter.StrategyPlotter(strat)

    strat.run()

    # Save the plot.
    plot.savePlot("/shark/backtest/" + ticker + ".png") 

    with open("/shark/backtest/" + ticker + ".html", 'w') as htmlFile:

        htmlFile.write("<html>")
        htmlFile.write("<head>")
        htmlFile.write("</head>")
        htmlFile.write("<body>")
        htmlFile.write("<h1>Strategy Performance - "+ticker+"</h1>") 
        htmlFile.write("<a href = '/shark/backtest/" + ticker + ".trade.log'>Trade Log</a>")
        htmlFile.write("<br />")
        htmlFile.write("<br />")
        htmlFile.write("<table border=1 style='width: 800px'>")
        htmlFile.write("<tr><th style='background-color: #E0E0E0' colspan='2'>Portfolio Summary</th></tr>") 
        htmlFile.write("<tr><td>Final portfolio value:</td><td>$%.2f</td></tr>" % strat.getResult())
        htmlFile.write("<tr><td>Cumulative returns:</td><td>%.2f %%</td></tr>" % (retAnalyzer.getCumulativeReturns()[-1] * 100))

        sharpeRatio = sharpeRatioAnalyzer.getSharpeRatio(0.05)

        htmlFile.write("<tr><td>Sharpe ratio:</td><td>%.2f</td></tr>" % (sharpeRatio))
        htmlFile.write("<tr><td>Max. drawdown:</td><td>%.2f %%</td></tr>" % (drawDownAnalyzer.getMaxDrawDown() * 100))
        htmlFile.write("<tr><td>Longest drawdown duration:</td><td>%s</td></tr>" % (drawDownAnalyzer.getLongestDrawDownDuration()))
        htmlFile.write("<tr><td style='background-color: #E8E8E8'>Total trades:</td><td>%d</td></tr>" % (tradesAnalyzer.getCount()))
        htmlFile.write("<tr><td style='text-align: right'>Wins:</td><td>%d</td></tr>" % (tradesAnalyzer.getProfitableCount()))
        htmlFile.write("<tr><td style='text-align: right'>Losses:</td><td>%d</td></tr>" % (tradesAnalyzer.getUnprofitableCount()))
        htmlFile.write("</table>")
        htmlFile.write("<br />")

        htmlFile.write("<img src = '/shark/backtest/" + ticker + ".png' />")

        if tradesAnalyzer.getCount() > 0:

            profits = tradesAnalyzer.getAll()

            htmlFile.write("<table border=1 style='width: 800px'>")
            htmlFile.write("<tr><th colspan='2' style='background-color: #E0E0E0'>Wins + Losses</th></tr>") 
            
            htmlFile.write("<tr><td>Avg. profit:</td><td>$%2.f</td></tr>" % (profits.mean()))
            htmlFile.write("<tr><td>Profits std. dev.:</td><td>$%2.f</td></tr>" % (profits.std()))
            htmlFile.write("<tr><td>Max. profit:</td><td>$%2.f</td></tr>" % (profits.max()))
            htmlFile.write("<tr><td>Min. profit:</td><td>$%2.f</td></tr>" % (profits.min()))

            returns = tradesAnalyzer.getAllReturns()

            htmlFile.write("<tr><td>Avg. return:</td><td>%2.f %%</td></tr>" % (returns.mean() * 100))
            htmlFile.write("<tr><td>Returns std. dev.:</td><td>%2.f %%</td></tr>" % (returns.std() * 100))
            htmlFile.write("<tr><td>Max. return:</td><td>%2.f %%</td></tr>" % (returns.max() * 100))
            htmlFile.write("<tr><td>Min. return:</td><td>%2.f %%</td></tr>" % (returns.min() * 100)) 
            
            htmlFile.write("</table>")
            htmlFile.write("<br />")

        if tradesAnalyzer.getProfitableCount() > 0:

            profits = tradesAnalyzer.getProfits()

            htmlFile.write("<table border=1 style='width: 800px'>")
            htmlFile.write("<tr><th colspan='2' style='background-color: #E0E0E0'>Wins</th></tr>") 
            
            htmlFile.write("<tr><td>Avg. profit:</td><td>$%2.f</td></tr>" % (profits.mean()))
            htmlFile.write("<tr><td>Profits std. dev.:</td><td>$%2.f</td></tr>" % (profits.std()))
            htmlFile.write("<tr><td>Max. profit:</td><td>$%2.f</td></tr>" % (profits.max()))
            htmlFile.write("<tr><td>Min. profit:</td><td>$%2.f</td></tr>" % (profits.min()))

            returns = tradesAnalyzer.getPositiveReturns()

            htmlFile.write("<tr><td>Avg. return:</td><td>%2.f %%</td></tr>" % (returns.mean() * 100))
            htmlFile.write("<tr><td>Returns std. dev.:</td><td>%2.f %%</td></tr>" % (returns.std() * 100))
            htmlFile.write("<tr><td>Max. return:</td><td>%2.f %%</td></tr>" % (returns.max() * 100))
            htmlFile.write("<tr><td>Min. return:</td><td>%2.f %%</td></tr>" % (returns.min() * 100))

            
            htmlFile.write("</table>")
            htmlFile.write("<br />")

        if tradesAnalyzer.getUnprofitableCount() > 0:

            losses = tradesAnalyzer.getLosses()
            
            htmlFile.write("<table border=1 style='width: 800px'>")
            htmlFile.write("<tr><th colspan='2' style='background-color: #E0E0E0'>Losses</th></tr>") 

            htmlFile.write("<tr><td>Avg. loss:</td><td>$%2.f</td></tr>" % (losses.mean()))
            htmlFile.write("<tr><td>Losses std. dev.:</td><td>$%2.f</td></tr>" % (losses.std()))
            htmlFile.write("<tr><td>Max. loss:</td><td>$%2.f</td></tr>" % (losses.min()))
            htmlFile.write("<tr><td>Min. loss:</td><td>$%2.f</td></tr>" % (losses.max()))

            returns = tradesAnalyzer.getNegativeReturns()

            htmlFile.write("<tr><td>Avg. return:</td><td>%2.f %%</td></tr>" % (returns.mean() * 100))
            htmlFile.write("<tr><td>Returns std. dev.:</td><td>%2.f %%</td></tr>" % (returns.std() * 100))
            htmlFile.write("<tr><td>Max. return:</td><td>%2.f %%</td></tr>" % (returns.max() * 100))
            htmlFile.write("<tr><td>Min. return:</td><td>%2.f %%</td></tr>" % (returns.min() * 100))
    
            htmlFile.write("</table>")
            htmlFile.write("<br />")

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
    
    smaPeriod = 50

    run_strategy(ticker, shares, capital, smaPeriod)
