#!/usr/bin/python3

# Using jinja templating engine, it gernates the trade log based on the json file using apache drill.
# Drill is used to provide scability options in the future.

from jinja2 import Template

import datetime
import sys
import subprocess
import argparse
import pandas

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
        parser.add_argument("-f", "--htmlFile", help="Name of the HTML file to save the report as (or otherwise it goes to STDIO).")
        args = parser.parse_args()

        if not args.ticker:

            print ("UNKNOWN - No ticker specified")
            sys.exit(UNKNOWN)
    
        ticker = args.ticker
   
        # Select all trades.

        tradeRecord = drill.query("SELECT * FROM dfs.tradelog.`" + ticker + ".trade.log`")
        df = tradeRecord.to_dataframe()

        # Count the total number of rows in the DF (represents the number of trades)

        index = df.index
        total_trades = len(index)

        # This is needed for the below.
        df["price"] = pandas.to_numeric(df['price'])

        # Get the most costly trade

        pos = df["price"].argmax()
        highest_trade = df["price"].iloc[pos]

        # Get the cheapest trade.

        pos = df["price"].argmin()
        lowest_trade = df["price"].iloc[pos]

        with open('/shark/bin/tradelog.html.jinja') as f:

            tmpl = Template(f.read())

            if args.htmlFile:
           
                with open(args.htmlFile, "w") as f:
                    
                    f.write(tmpl.render(
                        ticker = ticker, 
                        total_trades = total_trades,
                        highest_trade = highest_trade,
                        lowest_trade = lowest_trade,
                        x = df
                    ))
            
            else:
            
                print(tmpl.render(
                    ticker = ticker, 
                    total_trades = total_trades,
                    highest_trade = highest_trade,
                    lowest_trade = lowest_trade,
                    x = df
                ))
