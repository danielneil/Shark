#!/usr/bin/python

import pandas as pd
import datetime
import numpy as np
import sys
import argparse
import os

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "This plugin checks the simple moving average (SMA) for a stock. Based on the output, you can decide to set certain warning and critical threshold levels."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock.")
    parser.add_argument("-p", "--periods", help="Number of trading periods for which to compute against.")
    parser.add_argument("-r", "--raw", nargs='?', const=1, type=int, help="Just print the price minus pretty output.")
    parser.add_argument("-max", "--max", help="Warn if the result is greater than this threshold.")
    parser.add_argument("-min", "--min", help="Warn if the result is less than this threshold.")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    if not os.path.isfile('/atp/ticker-data/'+args.ticker+'.AX.txt'):
        print ("UNKNOWN - Ticker data file not found, exit...")
        sys.exit(UNKNOWN)

    if not args.periods:
        print ("UNKNOWN - Periods not supplied")
        sys.exit(UNKNOWN)

    ticker = args.ticker
    smaPeriod = int(args.periods)

    data = pd.read_csv('/atp/ticker-data/'+ticker+'.AX.txt')
    dataFrame = data['Adj Close']
    sma = np.round(dataFrame.rolling(smaPeriod).mean().iloc[-1], 2)

    returnCode = OK

    if args.raw:
        print(str(sma))
    else:
        if args.max and int(args.max) <  sma:
            print("WARNING - SMA($" + str(sma) + ") is above threshold " + str(args.max))
            returnCode = WARNING
        elif args.min and int(args.min) >  sma:
            print("WARNING - SMA($" + str(sma) + ") is below threshold " + str(args.min))
            returnCode = WARNING
        else:
            print("OK - $" + str(sma))

    sys.exit(returnCode)