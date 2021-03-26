#!/usr/bin/python3

import cgitb

# Using jinja templating engine, it gernates the transact log summary page with the json files using apache drill.

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

#####################################
# Header 

cgitb.enable()
print("Content-Type: text/html;charset=utf-8\r\n\r\n")

#####################################
# Body 

print("<h3>Transaction Summary</h3>")

drill = PyDrill(host='localhost', port=8047)

if not drill.is_active():
   
   raise ImproperlyConfigured('Please run Drill first')

totalTransactions = drill.query("select count(*) from `dfs.backtests`.`transactions`")

df = totalTransactions.to_dataframe()

index = df.index
transNumber = len(index)

print("<h2>Total Transactions - " + str(transNumber) + "</h2>")



