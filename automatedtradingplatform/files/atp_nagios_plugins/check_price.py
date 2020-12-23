#!/usr/bin/python

import pandas as pd
import datetime

import sys

if __name__ == "__main__":

    ticker = sys.argv[1]

    data = pd.read_csv('/atp/ticker-data/'+ticker+'.AX.txt')

    dataFrame = data['Adj Close']

    lastPrice = dataFrame.iloc[-1]
    yesterdayPrice = dataFrame.iloc[-2]

    if lastPrice > yesterdayPrice:
        print(lastPrice)
        sys.exit(0)
    else:
        print(lastPrice)
        sys.exit(2)


