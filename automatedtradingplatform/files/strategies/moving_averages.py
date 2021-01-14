#!/usr/bin/python

import pandas as pd
import datetime
import sys
import subprocess
import argparse

# Nagios constants. 

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "Example strategy: trigger a buy when the shorter simple moving average, crosses above the longer simple moving average"

strategy_name = "Moving Averages"

longer_sma_periods = 50
shorter_sma_periods = 10

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock in question")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    ticker = args.ticker 

    short_sma = subprocess.check_output(['/atp/plugins/check_sma.py', '--ticker', ticker, '--periods', str(shorter_sma_periods), '--raw'])
    long_sma = subprocess.check_output(['/atp/plugins/check_sma.py', '--ticker', ticker, '--periods', str(longer_sma_periods), '--raw'])

    if short_sma > long_sma:
       buy_str = "Buy Opportunity! - " + str(shorter_sma_periods) + " day SMA($" + str(short_sma).rstrip() + ") is above " + str(longer_sma_periods) + " day SMA ($" + str(long_sma).rstrip() + ")"
       print(buy_str)
       sys.exit(CRITICAL)

    print("No Opportunity Detected")
    
    sys.exit(OK)
