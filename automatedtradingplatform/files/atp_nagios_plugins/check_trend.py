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
    parser.add_argument("-1st", "--firstMA", help="First moving average (the shorter, e.g. 10 days)")
    parser.add_argument("-2nd", "--secondMA", help="Second moving average (the longer, e.g. 50 days)")
    parser.add_argument("-3rd", "--thirdMA", help="Third moving average (the longest. e.g. 100 days)")
    
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

    if not args.thirdMA:
        print("UNKNOWN - No third moving average found")
  
    ticker = args.ticker 
    firstMAarg = args.firstMA
    secondMAarg = args.secondMA
    thirdMAarg = args.thirdMA

    firstMA = subprocess.check_output(['/atp/nagios_plugins/check_sma.py', ticker, firstMAarg])
    secondMA = subprocess.check_output(['/atp/nagios_plugins/check_sma.py', ticker, secondMAarg])
    thirdMA = subprocess.check_output(['/atp/nagios_plugins/check_sma.py', ticker, thirdMAarg])

    if firstMA > secondMA and secondMA > thirdMA:
        print ("Uptrend Detected")
        sys.exit(OK)
    else:
        print ("Downtrend Detected")
        sys.exit(CRITICAL)

    sys.exit(0)
