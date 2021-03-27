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

# Number of total transactions.
totalTransactions = len(dataframe.index)

# Number of BUYS
dataframe.sort_values("action", inplace = True)
filter = dataframe["action"] == "BUY"
dataframe.where(filter, inplace = True)
totalBuys = len(dataframe.index)

# Reset the index (reset using reset_index() on the df didn't work? Anyone?
dataframe = dataframe.to_dataframe()

# Number of SELLS
dataframe.sort_values("action", inplace = True)
filter = dataframe["action"] == "SELL"
dataframe.where(filter, inplace = True)
totalSells = len(dataframe.index)

# Reset the index (reset using reset_index() on the df didn't work? Anyone?
dataframe = dataframe.to_dataframe()

print("<h3>Total transactions: " + str(totalTransactions) + "</h3>")
print("<h3>Total Buys: " + str(totalBuys) + "</h3>")
print("<h3>Total Sells: " + str(totalSells) + "</h3>")

print("<h3>highest SELL price transaction</h3>")
print("<h3>highest BUY price transaction</h3>")
print("<h3>lowest SELL price transaction</h3>")
print("<h3>Total number of shares exchanged in all transactions</h3>")
