#!/usr/bin/python3

# Summarises the backtest's transactions into a single web page.

import cgitb
import pandas
import sys 
from pydrill.client import PyDrill

#####################################
# Header - Don't edit. 

cgitb.enable()
print("Content-Type: text/html;charset=utf-8\r\n\r\n")

#####################################
# Body - Edit away. 

print("<h3>Transaction Summary</h3>")
print("<hr />")

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
totalVolume = df['quantity'].sum()

print("<h3>Total transactions: " + str(totalTransactions) + "</h3>")

print("<h3>Total Buys: " + str(totalBuys) + "</h3>")
print("<h3>Highest BUY: (ticker) " + str(highest_buy) + "</h3>")
print("<h3>Lowest BUY: " + str(lowest_buy) + "</h3>")

print("<h3>Total Sells: " + str(totalSells) + "</h3>")
print("<h3>Highest SELL: " + str(highest_sell) + "</h3>")
print("<h3>Lowest SELL: " + str(lowest_sell) + "</h3>")

print("<h3>Volume of shares exchanged: " + str(totalVolume) + " </h3>")
print("<h3>Value: </h3>")
