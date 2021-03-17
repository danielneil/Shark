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

cmd_arg_help = "Refreshes the backtest transaction UI for a specific ticker"

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

        tradeRecord = drill.query("SELECT * FROM dfs.backtests.`" + ticker + ".transaction.json`")

        df = tradeRecord.to_dataframe()

        # Count the total number of rows in the DF (represents the number of trades)

        index = df.index
        total_transactions = len(index)

        # This is needed for the below.
        df["price"] = pandas.to_numeric(df['price'])

        # Get the most costly BUY

        filter = df["action"] == 'BUY'
        df.where(filter, inplace = True)

        pos = df["price"].argmax()
        highest_buy = df["price"].iloc[pos]

        # Get the cheapest BUY.

        pos = df["price"].argmin()
        lowest_buy = df["price"].iloc[pos]

        # Reset the index (reset using reset_index() on the df didn't work? Anyone?
        df = tradeRecord.to_dataframe()
        df["price"] = pandas.to_numeric(df['price'])

        # Get the most costly SELL

        filter = df["action"] == 'SELL'
        df.where(filter, inplace = True)
        
        pos = df["price"].argmax()
        highest_sell = df["price"].iloc[pos]

        # Get the most cheapest SELL

        pos = df["price"].argmin()
        lowest_sell = df["price"].iloc[pos]

        # Reset the dataframe
        df = tradeRecord.to_dataframe()

        with open('/shark/bin/transaction.html.jinja') as f:

            tmpl = Template(f.read())

            if args.htmlFile:
           
                with open(args.htmlFile, "w") as f:
                    
                    f.write(tmpl.render(

                        ticker = ticker, 
                        total_transactions = total_transactions,
                        highest_buy = highest_buy,
                        lowest_buy = lowest_buy,
                        highest_sell = highest_sell,
                        lowest_sell = lowest_sell,
                        x = df

                    ))
            
            else:
            
                print(tmpl.render(

                    ticker = ticker, 
                    total_transactions = total_transactions,
                    highest_buy = highest_buy,
                    lowest_buy = lowest_buy,
                    highest_sell = highest_sell,
                    lowest_sell = lowest_sell,
                    x = df

                ))
