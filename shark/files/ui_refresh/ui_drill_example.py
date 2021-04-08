#!/usr/bin/python3

# Gets the number of records in the trade log - purely for example. 

import datetime
import sys
import subprocess
import argparse

from pydrill.client import PyDrill

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

drill = PyDrill(host='localhost', port=8047)

if not drill.is_active():
    raise ImproperlyConfigured('Please run Drill first')

cmd_arg_help = "Refreshes the backtest UI stuff for a specific ticker"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker of the stock in question.")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)
    
    ticker = args.ticker
    
    tradeCount = drill.query("SELECT count(datetime) FROM dfs.transactions.`" + ticker + ".trade.log`")

    df = tradeCount.to_dataframe()
    count = df.iloc[0,0]

    print(count)
