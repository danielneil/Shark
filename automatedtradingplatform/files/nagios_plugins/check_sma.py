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

cmd_arg_help = "Computes a simple moving average of a specific ASX ticker against a specific number of days."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock.")
    parser.add_argument("-d", "--days", help="Number of days for which to compute the SMA against.")
    parser.add_argument("-r", "--raw", nargs='?', const=1, type=int, help="Just print the price minus pretty output and return OK(0)")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    if not os.path.isfile('/atp/ticker-data/'+args.ticker+'.AX.txt'):
        print ("UNKNOWN - Ticker data file not found, exit...")
        sys.exit(UNKNOWN)

    if not args.days:
        print ("UNKNOWN - Days not supplied")
        sys.exit(UNKNOWN)

    ticker = args.ticker
    smaPeriod = int(args.days)

    data = pd.read_csv('/atp/ticker-data/'+ticker+'.AX.txt')

    dataFrame = data['Adj Close']

    smaResult = np.round(dataFrame.rolling(smaPeriod).mean().iloc[-1], 2)

    if args.raw:
        print(str(smaResult))
        sys.exit(OK)

    print ("$" + str(smaResult))

    sys.exit(OK)
