#!/usr/bin/python3

import requests 
import hashlib 
import os.path
import sys

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import sys
import argparse

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "This plugin monitors a website for changes. E.g.  the Investor Information section of a publicly listed company, or a page displaying news for a specific derivative."


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="ticker code of the stock")
    parser.add_argument("-w", "--website", help="URL of the website of interest")

    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    if not args.website:
        print("UNKNOWN - URL Missing")
        sys.exit(UNKNOWN)

    ticker = args.ticker
    url = args.website

    hashFile = "/atp/websites.hash"

    # Get the hash of the page on the other end of the URL

    page = requests.get(url, verify=False)

    websiteHash = hashlib.sha256(page.text.encode('utf-8')).hexdigest()

    with open(hashFile, "r+") as f:

        if websiteHash in f.read():

            print("Website - No changes detected")
            sys.exit(OK)

        else:

            f.seek(0)

            if url in f.read():

                print("Website - Changes Detected!")
                sys.exit(WARNING)

            else:

                print("Website - Added")
                f.write('"' + url + '",' + websiteHash + "\n")
                sys.exit(OK)
