#!/usr/bin/python

import pandas as pd
import numpy as np
import datetime
import argparse
import sys
import os

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "This plugin checks the VIX (Volatility Index) for a stock. Based on the output, you can decide to set certain warning and critical threshold levels."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    args = parser.parse_args()

    data = pd.read_csv('/shark/ticker-data/AXVI.csv')

    dataFrame = data['Adj Close']

    lastVix = np.round(dataFrame.iloc[-1], 2)

    print(str(lastVix))

    sys.exit(0)


