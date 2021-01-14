#!/usr/bin/python

import pandas as pd
import numpy as np
import datetime
import os
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
    parser.add_argument("-p", "--periods", help="Number of trading periods for which to compute against.")
    parser.add_argument("-max", "--max", help="Warn if the RSI is greater than this threshold.")
    parser.add_argument("-min", "--min", help="Warn if the RSI is less than this threshold.")
    parser.add_argument("-r", "--raw", nargs='?', const=1, type=int, help="Just print the price minus pretty output.")

    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)
    else:
        if not os.path.isfile('/atp/ticker-data/'+args.ticker+'.AX.txt'):
            print ("UNKNOWN - ticker data file not found")
            sys.exit(UNKNOWN)

    if not args.periods:
        print ("UNKNOWN - No rsi period found")
        sys.exit(UNKNOWN)

    ticker = args.ticker
    rsiPeriod = args.periods

    data = pd.read_csv('/atp/ticker-data/'+ticker+'.AX.txt')

    data['RSI'] = computeRSI(data['Adj Close'], int(rsiPeriod))
    df = data['RSI']
    
    rsi =  np.round(df.iloc[-1],2)

    returnCode = OK

    if args.raw:
        print(str(rsi))
    else:
        if args.max and int(args.max) <  rsi:
            print("WARNING - RSI(" + str(rsi) + ") is above threshold " + str(args.max))
            returnCode = WARNING
        elif args.min and int(args.min) >  rsi:
            print("WARNING - RSI(" + str(rsi) + ") is below threshold " + str(args.min))
            returnCode = WARNING
        else:
            print("OK - " + str(rsi))

    sys.exit(returnCode)