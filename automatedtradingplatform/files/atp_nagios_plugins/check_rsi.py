#!/usr/bin/python

import pandas as pd
import numpy as np
import datetime

import sys

if __name__ == "__main__":

    ticker = sys.argv[1]
    rsiPeriod = sys.argv[2]

    data = pd.read_csv('/atp/ticker-data/'+ticker+'.AX.txt')

    dataFrame = data['Adj Close']

    lastPrice = np.round(dataFrame.iloc[-1], 2)
    yesterdayPrice = np.round(dataFrame.iloc[-2], 2)

    if lastPrice > yesterdayPrice:
        percentageDiff = '{0:.2f}'.format(abs((yesterdayPrice/lastPrice * 100) -100)) 

        print("$" + str(lastPrice) + " (" + str(percentageDiff) + "%)")
        sys.exit(0)
    else:
        percentageDiff = '{0:.2f}'.format((lastPrice/yesterdayPrice * 100) -100)

        print("$" + str(lastPrice) + " (" + str(percentageDiff) + "%)")
        sys.exit(2)


