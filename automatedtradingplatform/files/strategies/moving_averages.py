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

cmd_arg_help = "Example strategy: buy when the first simple moving average, crosses above the second simple moving average"

strategy_name = "Moving Averages"

first_ma_days = 50
second_ma_days = 10

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock in question")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    ticker = args.ticker 

    firstSMAPeriod = subprocess.check_output(['/atp/nagios_plugins/check_sma.py', '--ticker', ticker, str(second_ma_days), '--raw'])
    secondSMAPeriod = subprocess.check_output(['/atp/nagios_plugins/check_sma.py', '--ticker', ticker, str(first_ma_days), '--raw'])

    if firstSMAPeriod > secondSMAPeriod:
       print("Buy Opportunity!")
       sys.exit(CRITICAL)

    print("No Opportunity Detected")
    
    sys.exit(OK)
