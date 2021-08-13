#!/usr/bin/python3

# Process the yaml configuration file, so we can regenerate it into something nagios understands.

import csv
import re
import yaml
import socket

##############################################################    

from io import StringIO

class StringBuilder:
    _file_str = None

    def __init__(self):
        self._file_str = StringIO()

    def Add(self, str):
        self._file_str.write(str)

    def __str__(self):
        return self._file_str.getvalue()

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
            
            hosts.Add("\ndefine host {\n")
            hosts.Add("\tuse stock\n")
            hosts.Add("\thost_name " + ticker + "\n")
            hosts.Add("\thostgroups " + instrument_group + "\n")
            hosts.Add("\taddress 127.0.0.1" + "\n")
            hosts.Add("\tregister 1" + "\n")
            hosts.Add("}\n")
            
            continue

        services.Add("\ndefine service {" + "\n")
        services.Add("\thost_name " + ticker + "\n")
        services.Add("\tservice_groups " + str(key) + "\n")
        
        # Add the parent node, and we'll prune duplicates after.
        service_group_defs.append(str(key))

        command_str = ""
        for k,v in value.items():

            yml_item = str(k)
            yml_value = str(v)
            
            # the descript will always be the first element.
            if yml_item == "DESCRIPTION":
                services.Add("\tservice_description " + yml_value+ "\n")
            elif yml_item == "PLUGIN":

                command_str = "check_command " + yml_value
            
                if yml_value == "check_backtest":

                    # Add a web link to the details of the backtest.
                    
                    hostname = socket.gethostname()
                    local_ip = socket.gethostbyname(hostname)

                    services.Add("\tnotes_url http://" + local_ip + "/shark/backtest/html/" + ticker + ".html" + "\n")
                    
                if yml_value == "check_strategy":
                    
                    # If this is the strategy command, add the event handler to perform the BUY order.
                    services.Add("\tevent_handler enter_trade")
                    
            else:
                 # print the command arguments
                command_str += "!" + yml_value

        services.Add("\t" + command_str + "\n")
        services.Add("\tmax_check_attempts 1" + "\n")
        services.Add("\tcheck_interval 5" + "\n")
        services.Add("\tretry_interval 3" + "\n")
        services.Add("\tcheck_period 24x7" + "\n")
        services.Add("\tnotification_interval 30" + "\n")
        services.Add("\tnotification_period 24x7" + "\n")
        services.Add("\tnotification_options w,c,r" + "\n")
        services.Add("\tcontact_groups admins" + "\n")
        services.Add("}\n" + "\n")

##############################################################    

service_group_defs = []
industry_groups = []

hosts = StringBuilder()
services = StringBuilder()

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

##############################################################    
# Print Hosts

print(hosts)

##############################################################   
# Print Services

print(services)
