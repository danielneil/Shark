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

cmd_arg_help = "Example strategy: trigger a buy when the mean reverts"

strategy_name = "Moving Averages"

rsi_low = 10
longer_sma_periods = 50
shorter_sma_periods = 10

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker of the stock to run the strategy against.")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    ticker = args.ticker 

    short_sma = subprocess.check_output(['/atp/plugins/check_sma.py', '--ticker', ticker, '--periods', str(shorter_sma_periods), '--raw'])
    long_sma = subprocess.check_output(['/atp/plugins/check_sma.py', '--ticker', ticker, '--periods', str(longer_sma_periods), '--raw'])
    rsi = subprocess.check_output(['/atp/plugins/check_rsi.py', '--ticker', ticker, '--periods', str(2),'--raw'])

    if short_sma < long_sma and rsi < rsi_low:

       buy_str = "Buy Opportunity! - " + str(shorter_sma_periods) + " day SMA($" + str(short_sma).rstrip() + ") is above " + str(longer_sma_periods) + " day SMA ($" + str(long_sma).rstrip() + ") and RSU("+rsi+")"
     
       print(buy_str)
       sys.exit(CRITICAL)

    print("No Opportunity")
    
    sys.exit(OK)
