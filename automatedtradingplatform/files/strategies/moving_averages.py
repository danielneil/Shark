#!/usr/bin/python

import pandas as pd
import datetime
import sys
import subprocess

# Our straegy is simple - buy when the first moving average, crosses above the second moving average

if __name__ == "__main__":

    ticker = sys.argv[1]

    firstSMAPeriod = subprocess.check_output(['/atp/nagios_plugins/check_sma.py', ticker, '10'])
    secondSMAPeriod = subprocess.check_output(['/atp/nagios_plugins/check_sma.py', ticker, '50'])

    if firstSMAPeriod > secondSMAPeriod:

            print("Buy Opportunity Detected")
            sys.exit(2)
    else:
            print("No Opportunity Detected")
            sys.exit(0)

    sys.exit(0)
