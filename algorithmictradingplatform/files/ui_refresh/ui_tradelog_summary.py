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


tradeRecord = drill.query("SELECT * FROM dfs.tradelogg`")

df = tradeRecord.to_dataframe()

