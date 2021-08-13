#!/usr/bin/python3

# Process the yaml configuration file, so we can regenerate it into something nagios understands.

import csv
import re
import yaml
import socket

##############################################################    

def process_instrument_config(a_dict):
    
    for key, value in a_dict.items():
        ticker = key
        if isinstance(value, dict):
            process_sub_config(value, ticker)

##############################################################                
            
def process_sub_config(a_dict,ticker):

    for key, value in a_dict.items():
        
        # First arg will be the INSTRUMENT_GROUP
        
        if str(key) == "GROUP":
            
            instrument_group = str(value)
            industry_groups.append(instrument_group)
            
            print("\ndefine host {")
            print("\tuse stock")
            print("\thost_name " + ticker)
            print("\thostgroups " + instrument_group)
            print("\taddress 127.0.0.1")
            print("\tregister 1")
            print("}")
            
            continue

        print("\ndefine service {")
        print("\thost_name " + ticker)
        print("\tservice_groups " + str(key))

        # Add the parent node, and we'll prune duplicates after.
        service_group_defs.append(str(key))

        command_str = ""
        for k,v in value.items():

            yml_item = str(k)
            yml_value = str(v)
            
            # the descript will always be the first element.
            if yml_item == "DESCRIPTION":
                print("\tservice_description " + yml_value)
            elif yml_item == "PLUGIN":

                command_str = "check_command " + yml_value
            
                if yml_value == "check_backtest":

                    # Add a web link to the details of the backtest.
                    
                    hostname = socket.gethostname()
                    local_ip = socket.gethostbyname(hostname)

                    print("\tnotes_url http://" + local_ip + "/shark/backtest/html/" + ticker + ".html")
                    
                if yml_value == "check_strategy":
                    
                    # If this is the strategy command, add the event handler to perform the BUY order.
                    print("\tevent_handler enter_trade")
                    
            else:
                 # print the command arguments
                command_str += "!" + yml_value

        print("\t" + command_str)
        print("\tmax_check_attempts 1")
        print("\tcheck_interval 5")
        print("\tretry_interval 3")
        print("\tcheck_period 24x7")
        print("\tnotification_interval 30")
        print("\tnotification_period 24x7")
        print("\tnotification_options w,c,r")
        print("\tcontact_groups admins")
        print("}\n")

##############################################################    

service_group_defs = []
industry_groups = []

with open ("/shark/conf/trading-config.yml", "r") as f:

    docs = yaml.safe_load(f)
    process_instrument_config(docs)
    
##############################################################    
    
# Remove duplicates from the industry groups

srted_industry_groups = sorted(set(industry_groups))

for ig in srted_industry_groups:

    print ("\ndefine hostgroup {")
    print ("\thostgroup_name " + ig )
    print ("\talias " + ig )
    print ("}")

##############################################################    
    
# Prune the duplicates from the service groups. 
sg_list = list ( dict.fromkeys(service_group_defs) )
for sg in sg_list:

    print("\ndefine servicegroup {")
    print("\tservicegroup_name " + sg )
    print("\talias " + sg )
    print("}")
