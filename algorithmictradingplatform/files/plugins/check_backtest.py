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
    parser.add_argument("-b", "--backtest", help="The file name of the backtest")
    parser.add_argument("-s", "--shares", help="The imaginary number of shares to use in the backtest")
    parser.add_argument("-c", "--capital", help="The imaginary amount of a capital which to use in the backtest")
    parser.add_argument("-n", "--noreport", help="Do not generate the back test reports", action="store_true", default=False)
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    if not args.backtest:
        print("UNKNOWN - No backtest file specified")
        sys.exit(UNKNOWN)

    if not args.shares:
        print("UNKNOWN - No imaginary shares specified")
        sys.exit(UNKNOWN)

    if not args.capital:
        print("UNKNOWN - No imaginary amount of capital specified")
        sys.exit(UNKNOWN)

    ticker = args.ticker 
    backtestFile = args.backtest
    capital = args.capital
    shares = args.shares

    if not os.path.isfile('/shark/strategies/backtesting/' + backtestFile):
        print ("UNKNOWN - Backtest file (" + backtestFile  + ") not found...")
        sys.exit(UNKNOWN)

    process = subprocess.Popen(['/shark/strategies/backtesting/' + backtestFile, '--ticker', ticker, '--shares', shares, '--capital', capital, args.noreport], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    stdout, stderr = process.communicate()

    exitcode = process.wait()

    print(stdout)

    sys.exit(exitcode)
