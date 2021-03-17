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
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    ticker = args.ticker

    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:

        channel = connection.channel()
        channel.basic_publish(exchange='', routing_key='BUYS', body="TICKER:" + ticker)
