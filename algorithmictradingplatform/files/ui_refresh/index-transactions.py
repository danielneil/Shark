#!/usr/bin/python3

# Summarises the backtest's transactions into a single web page.

from jinja2 import Template
import pandas
import sys
from pydrill.client import PyDrill
import cgitb

drill = PyDrill(host='localhost', port=8047)

if not drill.is_active():
   print("Please run Drill first")
   sys.exit(1)

# Select all the transactions with SQL, and we'll manipulate with the pandas functions.
transactions = drill.query("select * from `dfs.backtests`.`transactions`")
dataframe = transactions.to_dataframe()

# Convert to ints.
dataframe["quantity"] = pandas.to_numeric(dataframe["quantity"])
dataframe["quantity"] = pandas.to_numeric(dataframe["price"])

# ----------- Number of total transactions.

totalTransactions = len(dataframe.index)

# ----------- Number of BUYS

buy_subset = dataframe[dataframe["action"] == "BUY"]
totalBuys = len(buy_subset)

# ----------- Number of SELLS

sell_subset = dataframe[dataframe["action"] == "SELL"]
totalSells = len(sell_subset)

# ----------- Highest BUY

highest_buy_subset = dataframe[dataframe["action"] == "BUY"]
highest_buy_df = highest_buy_subset.max()
highest_buy_ticker = highest_buy_df["ticker"]
highest_buy = highest_buy_df["price"]

# ----------- Highest Sell

highest_sell_subset = dataframe[dataframe["action"] == "SELL"]
highest_sell_df = highest_sell_subset.max()
highest_sell_ticker = highest_sell_df["ticker"]
highest_sell = highest_sell_df["price"]

# ----------- Lowest BUY

lowest_buy_subset = dataframe[dataframe["action"] == "BUY"]
lowest_buy_df = lowest_buy_subset.min()
lowest_buy_ticker = lowest_buy_df["ticker"]
lowest_buy = lowest_buy_df["price"]

# ----------- Lowest SELL

lowest_sell_subset = dataframe[dataframe["action"] == "SELL"]
lowest_sell_df = lowest_sell_subset.min()
lowest_sell_ticker = lowest_sell_df["ticker"]
lowest_sell = lowest_sell_df["price"]

df = transactions.to_dataframe()

# ----------- Volume of shares exchanged
totalVolume = sum(df['quantity'])

# wrong but change a place holder to come back to
totalValue = 0

# Send the HTML headers.
cgitb.enable()
print("Content-Type: text/html;charset=utf-8\r\n\r\n")

# Drop the duplicate tickers - we just want a list of them.
dataframe = dataframe.drop_duplicates('ticker', keep="first", inplace=False)

with open('/shark/bin/index-transaction.html.jinja') as f:

	tmpl = Template(f.read())
            
	print(tmpl.render(
		totalTransactions = totalTransactions,
	        totalBuys = totalBuys,
	        highest_buy = highest_buy,
                lowest_buy = lowest_buy,
                totalSells  = totalSells,
	        highest_sell = highest_sell,
	        lowest_sell = lowest_sell,
	        totalVolume = totalVolume,
	        totalValue  = totalValue,
		x = dataframe,
		highest_buy_ticker = highest_buy_ticker,
		lowest_buy_ticker = lowest_buy_ticker,
		highest_sell_ticker = highest_sell_ticker,
		lowest_sell_ticker = lowest_sell_ticker
	))
