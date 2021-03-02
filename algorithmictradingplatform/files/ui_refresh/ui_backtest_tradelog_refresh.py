#!/usr/bin/python3

# Using jinja templating engine, it gernates the trade log based on the json file using apache drill.
# Drill is used to provide scability options in the future.

from jinja2 import Template

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

    with open('tradelog.html.jinja') as f:

        tmpl = Template(f.read())

        print(tmpl.render(
            ticker = ticker,
            x = df
        ))
