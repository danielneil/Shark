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

highest_buy_subset = dataframe[dataframe["price"] == "BUY"]
highest_buy = highest_buy_subset['price'].max()

# ----------- Highest Sell

highest_sell_subset = dataframe[dataframe["price"] == "SELL"]
highest_sell = highest_sell_subset['price'].max()

# ----------- Lowest BUY

lowest_buy_subset = dataframe[dataframe["price"] == "BUY"]
lowest_buy = lowest_buy_subset['price'].min()

# ----------- Lowest SELL

lowest_sell_subset = dataframe[dataframe["price"] == "SELL"]
lowest_sell = lowest_sell_subset['price'].min()

# ----------- Volume of shares exchanged
totalVolume = sum(dataframe['quantity'])

# wrong but change a place holder to come back to
totalValue = sum(dataframe['quantity'])

# Send the HTML headers.
cgitb.enable()
print("Content-Type: text/html;charset=utf-8\r\n\r\n")

dataframe = dataframe.drop_duplicates(subset='ticker', keep="first", inplace=False)

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
		x = dataframe
	))
