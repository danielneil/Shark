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

cmd_arg_help = 'This executes the strategy code. For a simple strategy, see the template for an example'

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock in question")
    parser.add_argument("-s", "--strategy", help="The file name of the custom strategy")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    if not args.strategy:
        print("UNKNOWN - No strategy file specified")
        sys.exit(UNKNOWN)

    ticker = args.ticker 
    strategyFile = args.strategy

    if not os.path.isfile('/atp/strategies/' + strategyFile):
        print ("UNKNOWN - Strategy file (" + strategyFile  + ") not found...")
        sys.exit(UNKNOWN)

    process = subprocess.Popen(['/atp/strategies/' + strategyFile, '--ticker', ticker], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    stdout, stderr = process.communicate()

    exitcode = process.wait()

    print(stdout)

    sys.exit(exitcode)
