#!/usr/bin/python3

import requests 
import hashlib 
import os.path
import sys

# Checks for changes in the website of interest using checksums, 
# and informs if changes have been detected. 
# Websites of interest are associated with a specific ticker.

if __name__ == "__main__":

    ticker = sys.argv[1] 
    url = sys.argv[2]

    # Get the hash of the page on the other end of the URL
    page = requests.get(url)
    websiteHash = hashlib.sha256(page.text.encode('utf-8')).hexdigest()
    
    fileName = "/tmp/.atp/websites/" + ticker

    # If this is a new ticker, just add it.
    if not os.path.isfile(fileName):
        with open(fileName, 'w') as f: 
            f.write(url + "," + websiteHash)
    else:
        with open(fileName) as f:
            if websiteHash in f.read():
                print("Website has no new updates")
                sys.exit(0)


