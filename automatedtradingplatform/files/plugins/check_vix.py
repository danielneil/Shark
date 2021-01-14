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

cmd_arg_help = "Get the VIX (Volatility Index)."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    args = parser.parse_args()

    data = pd.read_csv('/atp/ticker-data/AXVI.csv')

    dataFrame = data['Adj Close']

    lastVix = np.round(dataFrame.iloc[-1], 2)

    print(str(lastVix))

    sys.exit(0)


