#!/usr/bin/python3

import requests 
import hashlib 
import os.path
import subprocess
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import sys
import argparse

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "This plugin monitors a website of interest for changes. E.g. the investors section of a publicly listed company's website. By default, it performs a SHA256 of the website's source code. It can ignore specific lines to overcome a website which may generate dynamic content upon each load. For more complex websites, the plugin can compare checksums of screenshots for webpages."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-u", "--url", help="URL of the website of interest.")
    parser.add_argument("-c", "--checksum", help="The expected checksum, alarms if mismatch.")
    parser.add_argument("-l", "--ignoreLine", help="Ignore a specific line of the returned source code (")
    parser.add_argument("-g", "--generate", nargs='?', const=1, type=int, help="Get the checksum for a specific website. Used to create/refresh checksums")
    parser.add_argument("-s", "--screenshot", nargs='?', const=1, type=int, help="Instead of diffing the source code of a webpage (default), use a checksum of a screenshot instead")

    args = parser.parse_args()

    websiteHash = None

    if not args.url:
        print("UNKNOWN - URL Missing")
        sys.exit(UNKNOWN)

    url = args.url

    # Get the hash of the page (source code) on the other end of the URL

    if not args.screenshot:

        page = subprocess.check_output(["curl", "-s", url])

        sha256_hash = hashlib.sha256()
        sha256_hash.update(page)
        websiteHash = sha256_hash.hexdigest()

    else:
       
        tmp_store = "/tmp/" + re.sub(r'\W+', '', url) + ".png"
        subprocess.check_output(["/usr/bin/wkhtmltoimage", "-q",  url, tmp_store])

        with open(tmp_store, "rb") as screen_shot_file:

            content = screen_shot_file.read()
            
            sha256_hash = hashlib.sha256()
            sha256_hash.update(content)
            websiteHash = sha256_hash.hexdigest()

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
