#!/usr/bin/python

import pandas as pd
import datetime

import sys

if __name__ == "__main__":

    ticker = sys.argv[1]

    data = pd.read_csv('/atp/ticker-data/'+ticker+'.AX.txt')

    dataFrame = data['Adj Close']

    print (dataFrame.iloc[-1])
