a:6:{i:0;a:3:{i:0;s:14:"document_start";i:1;a:0:{}i:2;i:0;}i:1;a:3:{i:0;s:6:"header";i:1;a:3:{i:0;s:28:"Strategy: moving_averages.py";i:1;i:1;i:2;i:1;}i:2;i:1;}i:2;a:3:{i:0;s:12:"section_open";i:1;a:1:{i:0;i:1;}i:2;i:1;}i:3;a:3:{i:0;s:4:"code";i:1;a:3:{i:0;s:1366:"
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
    parser.add_argument("-t", "--ticker", help="Ticker of the stock to run the strategy against.")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    ticker = args.ticker 

    short_sma = subprocess.check_output(['/shark/plugins/check_sma.py', '--ticker', ticker, '--periods', str(shorter_sma_periods), '--raw'])
    long_sma = subprocess.check_output(['/shark/plugins/check_sma.py', '--ticker', ticker, '--periods', str(longer_sma_periods), '--raw'])

    if short_sma > long_sma:

       buy_str = "Buy Opportunity! - " + str(shorter_sma_periods) + " day SMA($" + str(short_sma).rstrip() + ") is above " + str(longer_sma_periods) + " day SMA ($" + str(long_sma).rstrip() + ")"
       print(buy_str)
       sys.exit(CRITICAL)

    print("No Opportunity")

    sys.exit(OK)
 ";i:1;s:6:"python";i:2;N;}i:2;i:50;}i:4;a:3:{i:0;s:13:"section_close";i:1;a:0:{}i:2;i:1431;}i:5;a:3:{i:0;s:12:"document_end";i:1;a:0:{}i:2;i:1431;}}