#!/usr/bin/python

import pandas as pd
import datetime
import subprocess
import os
import sys
import argparse

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = 'This executes the backtest code. For a simple backtest example, see the template'

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock in question")
    parser.add_argument("-s", "--backtest", help="The file name of the backtest")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    if not args.strategy:
        print("UNKNOWN - No backtest file specified")
        sys.exit(UNKNOWN)

    ticker = args.ticker 
    backtestFile = args.strategy

    if not os.path.isfile('/atp/backtests/' + backtestFile):
        print ("UNKNOWN - Backtest file (" + backtestFile  + ") not found...")
        sys.exit(UNKNOWN)

    process = subprocess.Popen(['/atp/backtests/' + backtestFile, '--ticker', ticker], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    stdout, stderr = process.communicate()

    exitcode = process.wait()

    print(stdout)

    sys.exit(exitcode)
