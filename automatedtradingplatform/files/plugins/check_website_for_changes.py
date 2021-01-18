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

cmd_arg_help = "This plugin monitors a website of interest for changes. E.g. the investors section of a publicly listed company's website. It performs a SHA256 of the website's source code. It can ignore specific lines to overcome a website which may generate dynamic content per load."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-u", "--url", help="URL of the website of interest.")
    parser.add_argument("-c", "--checksum", help="The expected checksum, alarms if mismatch.")
    parser.add_argument("-l", "--ignoreLine", help="Ignore a specific line of the returned source code")
    parser.add_argument("-g", "--generate", nargs='?', const=1, type=int, help="Get the checksum for a specific website. Used to create/refresh checksums")

    args = parser.parse_args()

    if not args.url:
        print("UNKNOWN - URL Missing")
        sys.exit(UNKNOWN)

    url = args.url

    # Get the hash of the page on the other end of the URL

    page = requests.get(url, verify=False)

    websiteHash = hashlib.sha256(page.text.encode('utf-8')).hexdigest()

    if args.generate:
        print(websiteHash)
        sys.exit(OK)

    if not args.checksum:
        print("UNKNOWN - No checksum found")
        sys.exit(UNKNOWN)

    if args.checksum == websiteHash:
        print("OK - No changes detected")
        sys.exit(OK)
    else:
        print("CRITICAL - Changes Detected")
        sys.exit(CRITICAL)

