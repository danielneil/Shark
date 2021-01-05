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

cmd_arg_help = "This plugin computes the relative strength index (RSI) for a stock."

def computeRSI (data, time_window):
    diff = data.diff(1).dropna()        # diff in one field(one day)

    #this preservers dimensions off diff values
    up_chg = 0 * diff
    down_chg = 0 * diff
    
    # up change is equal to the positive difference, otherwise equal to zero
    up_chg[diff > 0] = diff[ diff>0 ]
    
    # down change is equal to negative deifference, otherwise equal to zero
    down_chg[diff < 0] = diff[ diff < 0 ]
    
    # check pandas documentation for ewm
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html
    # values are related to exponential decay
    # we set com=time_window-1 so we get decay alpha=1/time_window
    up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    
    rs = abs(up_chg_avg/down_chg_avg)
    rsi = 100 - 100/(1+rs)
    return rsi

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    
    parser.add_argument("-t", "--ticker", help="ticker code of the stock")
    parser.add_argument("-r", "--rsiPeriod", help="RSI period of which to base the calculation upon.")
    parser.add_argument("-max", "--maxRSI", help="Warn if the RSI is greater than this threshold.")
    parser.add_argument("-min", "--minRSI", help="Warn if the RSI is less than this threshold.")

    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    if not args.rsiPeriod:
        print ("UNKNOWN - No rsi period found")
        sys.exit(UNKNOWN)

    ticker = args.ticker
    rsiPeriod = args.rsiPeriod

    maxRSI = False
    minRSI = False

    if args.maxRSI:
        maxRSI = int(args.maxRSI)

    if args.minRSI:
        minRSI = int(args.minRSI)
    
    data = pd.read_csv('/atp/ticker-data/'+ticker+'.AX.txt')

    data['RSI'] = computeRSI(data['Adj Close'], int(rsiPeriod))
    
    df = data['RSI']
    
    rsiValue =  np.round(df.iloc[-1],2)
    rsiValueStr = str(rsiValue)

    # If the min or max arn't suppled, just report the RSI and exit.
    if not args.maxRSI and not args.minRSI:
        print(rsiValueStr)
        sys.exit(OK)        
    
    if maxRSI and rsiValue > maxRSI:
        print("WARNING - RSI(" + rsiValueStr + ") is above " + str(maxRSI))
        sys.exit(WARNING)
    
    if minRSI and rsiValue < minRSI:
        print("WARNING - RSI(" + rsiValueStr + ") is below " + str(minRSI))
        sys.exit(WARNING)
    
    print("OK - RSI(" + rsiValueStr + ")")
    sys.exit(OK)
