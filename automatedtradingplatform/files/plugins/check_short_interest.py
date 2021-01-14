#!/usr/bin/python

import sys
import os
import argparse

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "Alarms on the short interest of a specific ASX ticker."
short_sell_file = "/atp/ticker-data/shortsell.txt"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    else:
        if not os.path.isfile(short_sell_file):
            print ("UNKNOWN - short interest data file not found")
            sys.exit(UNKNOWN)

    ticker = args.ticker

    with open(short_sell_file) as shorts_file:
        if ticker in shorts_file.read():
            print("WARNING - Short interest for " + ticker + " found")
            sys.exit(WARNING)
        else:
            print("OK - No short interest for ticker " + ticker + " found.")
            sys.exit(OK)
