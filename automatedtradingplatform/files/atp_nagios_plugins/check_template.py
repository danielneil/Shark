#!/usr/bin/python

import pandas as pd
import numpy as np
import datetime

import sys
import argparse

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "This is a template for a python check for the trading platform, make it as descriptive as possible as it will be used to generate documentation"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="ticker code of the stock")

    args = parser.parse_args()

    if args.ticker:
        print ("OK - Ticker: " + args.ticker)
        sys.exit(OK)

    else:
        print ("CRITICAL - No ticker found")
        sys.exit(CRITICAL)


print ("Something went wrong")
sys.exit(UNKNOWN)

