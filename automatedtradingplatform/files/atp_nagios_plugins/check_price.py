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

cmd_arg_help = "Gets the latest price of a stock."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock")
    parser.add_argument("-r", "--raw", nargs='?', const=1, type=int, help="Just print the latest price. Will always return OK(0)")

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

    if args.raw:
        print(lastPrice)
        sys.exit(OK)


    if lastPrice > yesterdayPrice:
        percentageDiff = '{0:.2f}'.format(abs((yesterdayPrice/lastPrice * 100) -100)) 

        print("$" + str(lastPrice) + " (" + str(percentageDiff) + "%)")
        sys.exit(OK)
    else:
        percentageDiff = '{0:.2f}'.format((lastPrice/yesterdayPrice * 100) -100)

        print("$" + str(lastPrice) + " (" + str(percentageDiff) + "%)")
        sys.exit(CRITICAL)
