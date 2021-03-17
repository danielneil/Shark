#!/usr/bin/python3

import pika
import datetime
import sys
import argparse
import os

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "Send a BUY order to the queue in RabbitMQ"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock.")    
    parser.add_argument("-ss", "--servicestate", help="OK/WARNING/UNKNOWN/CRITICAL") 
    parser.add_argument("-st", "--statetype", help="SOFT/HARD") 
    parser.add_argument("-sa", "--serviceattempt", help="1/2/3")
    
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    if not args.servicestate:
        print ("UNKNOWN - No servicestate found")
        sys.exit(UNKNOWN)       
    
    if not args.statetype:
        print ("UNKNOWN - No statetype found")
        sys.exit(UNKNOWN)    
    
    if not args.serviceattempt:
        print ("UNKNOWN - No serviceattempt found")
        sys.exit(UNKNOWN)    
    
    ticker = args.ticker

    if not args.servicestate == "CRITICAL":
        sys.exit(exitcode)
        
    if not args.statetype == "HARD":    
        if args.statetype == "SOFT" and not int(args.serviceattempt) == 3:
            sys.exit(exitcode)
    
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:

        channel = connection.channel()
        channel.basic_publish(exchange='', routing_key='BUYS', body="TICKER:" + ticker)
