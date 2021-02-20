#!/usr/bin/python3

# Builds the nagios configuration based on the ticker data.

import csv
import re
import yaml

# Open up our excludes file so we know which tickers to skip.

excluded_tickers = []

with open('/atp/excluded_tickers.txt') as exclude_file:

    while True:
        ticker = exclude_file.readline().rstrip()

        if not ticker:
            break

        excluded_tickers.append(ticker)


with open ('/atp/ASX_Listed_Companies.csv','r') as csvfile:
    tickerreader = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    # skip the first row.
    next(tickerreader)

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
                use stock
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


# Process the yaml configuration file, so we can regenerate it into something nagios understands.
# This sux so much, if someone can help me rewrite this POS that'd be greatttttt.
def process_ticker_config(a_dict):
    
    for key, value in a_dict.items():
        ticker = key
        if isinstance(value, dict):
            process_service_config(value, ticker)

    # Prune the duplicates from the service groups. 
    sg_list = list ( dict.fromkeys(service_group_defs) )

    for sg in sg_list:

        print("define servicegroup {")
        print("\tservicegroup_name " + sg)
        print("\talias " + sg)
        print("}")

def process_service_config(a_dict,ticker):

    for key, value in a_dict.items():

        print("\ndefine service {")
        print("\thost_name " + ticker)
        print("\tservice_groups " + str(key))

        # Add the parent node, and we'll prune duplicates after.
        service_group_defs.append(str(key))

        command_str = ""
        for k,v in value.items():

            # the descript will always be the first element.
            if str(k) == "description":
                print("\tservice_description " + str(v))
            else:
                if str(k) == "check_command":
                    command_str = "check_command " + str(v)
                else:
                    # print the command arguments
                    command_str += "!" + str(v)

        print("\t" + command_str)
        print("\tmax_check_attempts 5")
        print("\tcheck_interval 5")
        print("\tretry_interval 3")
        print("\tcheck_period 24x7")
        print("\tnotification_interval 30")
        print("\tnotification_period 24x7")
        print("\tnotification_options w,c,r")
        print("\tcontact_groups admins")
        print("}\n")

# Store services groups
service_group_defs = []

with open ("/atp/ticker-config.yml", "r") as f:

    docs = yaml.safe_load(f)
    process_ticker_config(docs)


