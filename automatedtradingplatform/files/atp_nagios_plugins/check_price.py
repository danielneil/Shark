#!/usr/bin/python

import pandas as pd
import numpy as np
import datetime
import argparse
import sys
import os

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "This plugin computes the relative strength index (RSI) for a stock."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="ticker code of the stock")
    args = parser.parse_args()


    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    else:
        if not os.path.isfile('/atp/ticker-data/'+args.ticker+'.AX.txt'):
            print ("UNKNOWN - ticker data file not found")
            sys.exit(UNKNOWN)

    ticker = args.ticker

    data = pd.read_csv('/atp/ticker-data/'+ticker+'.AX.txt')

    dataFrame = data['Adj Close']

    lastPrice = np.round(dataFrame.iloc[-1], 2)
    yesterdayPrice = np.round(dataFrame.iloc[-2], 2)

    if lastPrice > yesterdayPrice:
        percentageDiff = '{0:.2f}'.format(abs((yesterdayPrice/lastPrice * 100) -100)) 

        print("$" + str(lastPrice) + " (" + str(percentageDiff) + "%)")
        sys.exit(0)
    else:
        percentageDiff = '{0:.2f}'.format((lastPrice/yesterdayPrice * 100) -100)

        print("$" + str(lastPrice) + " (" + str(percentageDiff) + "%)")
        sys.exit(2)
