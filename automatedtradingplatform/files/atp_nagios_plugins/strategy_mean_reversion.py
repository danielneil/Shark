#!/usr/bin/python

import pandas as pd
import datetime
import sys
import subprocess

# Our straegy is simple - buy when the first moving average, crosses above the second moving average

if __name__ == "__main__":

    ticker = sys.argv[1]
    rsiArg = int(sys.argv[2])

    firstSma = int(sys.argv[3])
    secondSma = int(sys.argv[4])

    rsiMin = int(sys.argv[5])
    rsiMax = int(sys.argv[6])

    firstSMAPeriod = subprocess.check_output(['/atp/nagios_plugins/check_sma.py', ticker, firstSma])
    secondSMAPeriod = subprocess.check_output(['/atp/nagios_plugins/check_sma.py', ticker, secondSma])
    rsiValue = subprocess.check_output(['/atp/nagios_plugins/check_rsi.py' ticker, rsiArg, firstSma, secondSMA, 

    if firstSMAPeriod > secondSMAPeriod:

            print("Short Opportunity Detected")
            sys.exit(2)

    else:
            print("Long Opportunity Detected")
            sys.exit(0)

    sys.exit(0)
