#!/usr/bin/python

# Builds the nagios configuration based on the ticker data.

import csv
import re

# Open up our excludes file so we know which tickers to skip.

excluded_tickers = []

with open('/atp/excluded_tickers.txt') as exclude_file:

    while True:
        ticker = exclude_file.readline().rstrip()

        if not ticker:
            break

        excluded_tickers.append(ticker)


with open ('/atp/ASX_Listed_Companies.csv', newline='') as csvfile:
    tickerreader = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    industry_groups = []
    tickers = []

    # Spit out tickers and add them to their industry groups.
    for row in tickerreader:

        ticker = row[0]
        industry_group = row[3]

        # Check if the ticker is in our exclude list
        if ticker in excluded_tickers:
            continue

        cleaned_industry_group_str = re.sub('\W', '', industry_group)

        print( """
            define host {
                use linux-server
                host_name """+ticker+"""
                hostgroups """ +cleaned_industry_group_str+"""
                address 127.0.0.1
                register 1
            }
        """)

        industry_groups.append(industry_group)

# Remove duplicates from the industry groups
industry_groups = sorted(set(industry_groups))

for industry_group in industry_groups:

    cleaned_industry_group = re.sub('\W', '', industry_group)

    print ( """
        define hostgroup {
            hostgroup_name """ + cleaned_industry_group + """
            alias """ + industry_group + """
        }
    """)

