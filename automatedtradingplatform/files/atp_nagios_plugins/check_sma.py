#!/usr/bin/python

import pandas as pd
import datetime
import numpy as np

import sys

if __name__ == "__main__":

    ticker = sys.argv[1]
    smaPeriod = int(sys.argv[2])

    data = pd.read_csv('/atp/ticker-data/'+ticker+'.AX.txt')

    dataFrame = data['Adj Close']

    smaResult = np.round(dataFrame.rolling(smaPeriod).mean().iloc[-1], 2)

    print (smaResult)

    sys.exit(0)
