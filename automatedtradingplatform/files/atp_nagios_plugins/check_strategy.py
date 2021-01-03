#!/usr/bin/python

import pandas as pd
import datetime
import subprocess

import sys
import argparse

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "This strategy is simple moving averages, buy when the first moving average, crosses above the second. Opposite for shorts."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock")
    parser.add_argument("-f", "--firstMA", help="First moving average (the shorter, e.g. 10 days)")
    parser.add_argument("-s", "--secondMA", help="Second moving average (the longer, e.g. 50 days)")
    
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    if not args.firstMA:
        print ("UNKNOWN - No first moving average found")
        sys.exit(UNKNOWN)

    if not args.secondMA:
        print ("UNKNOWN - No second moving average found")
        sys.exit(UNKNOWN)
  
    ticker = args.ticker 
    firstMA = args.firstMA
    secondMA = args.secondMA

    firstSMAPeriod = subprocess.check_output(['/atp/nagios_plugins/check_sma.py', ticker, firstMA])
    secondSMAPeriod = subprocess.check_output(['/atp/nagios_plugins/check_sma.py', ticker, secondMA])

    if firstSMAPeriod > secondSMAPeriod:

            print("Long Opportunity")
            sys.exit(WARNING)
    else:
            print("Short Opportunity")
            sys.exit(OK)

    sys.exit(0)
