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

cmd_arg_help = "Refreshes the backtest traderecord UI for a specific ticker"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker of the stock in question.")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)
    
    ticker = args.ticker
    
    tradeRecord = drill.query("SELECT * FROM dfs.tradelog.`" + ticker + ".trade.log`")

    df = tradeRecord.to_dataframe()

    for index, row in df.iterrows():
        print(row["datetime"], row["action"], row["ticker"], row["quantity"], row["price"])
