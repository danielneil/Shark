#!/usr/bin/python

import pandas as pd
import numpy as np
import datetime

import sys

if __name__ == "__main__":

    data = pd.read_csv('/atp/ticker-data/AXVI.csv')

    dataFrame = data['Adj Close']

    lastVix = np.round(dataFrame.iloc[-1], 2)

    print(str(lastVix))

    sys.exit(0)


