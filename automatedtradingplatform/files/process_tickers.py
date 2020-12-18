#!/usr/bin/python

# Builds the nagios configuration based on the ticker data.

import csv

with open ('ASX_Listed_Companies.csv', newline='') as csvfile:
    tickerreader = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    # Skip the first row.
    next(tickerreader)

    for row in tickerreader:
        ticker = row[0]


        print( """
            define host {
                use linux-server
                host_name """+ticker+"""
                address 127.0.0.1
                register 1
            }
        """)
