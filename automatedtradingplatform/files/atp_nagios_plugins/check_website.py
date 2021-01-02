#!/usr/bin/python3

import requests 
import hashlib 
import os.path
import sys

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Checks for changes in the website of interest using checksums, 
# and informs if changes have been detected. 
# Websites of interest are associated with a specific ticker.

if __name__ == "__main__":

    ticker = sys.argv[1] 
    url = sys.argv[2]

    hashFile = "/atp/websites.hash"

    # Get the hash of the page on the other end of the URL

    page = requests.get(url, verify=False)

    websiteHash = hashlib.sha256(page.text.encode('utf-8')).hexdigest()

    with open(hashFile, "r+") as f:

        if websiteHash in f.read():

            print("Website - No changes detected")
            sys.exit(0)

        else:

            f.seek(0)

            if url in f.read():

                print("Website - Changes Detected!")
                sys.exit(2)

            else:

                print("Website - Added")
                f.write('"' + url + '",' + websiteHash + "\n")
                sys.exit(0)
