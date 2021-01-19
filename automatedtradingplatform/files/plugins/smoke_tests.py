#!/usr/bin/python

import subprocess
import sys

ERROR= 1
OK= 0

########################################################################
# Ticker Arg check
def check_ticker_arg(check_plugin):
	try:

		rsiCheck = float(subprocess.check_output([check_plugin]))
		print("Error, a ticker was not supplied, and therefore should have thrown an error, exiting...")	
		sys.exit(ERROR)

	except subprocess.CalledProcessError as e:

		if "UNKNOWN - No ticker found" == e.output.rstrip():
			print("OK - a ticker was not supplied and threw an error.")
		else:

			print("ERROR - a ticker was not supplied and something went wrong, exiting...")
			print(e.output)
			sys.exit(ERROR)

########################################################################
# Check RSI 

print("########################################################################")
print("# Check RSI")
print("########################################################################")

TICKER="CBA"
EXPECTED_RSI=62.95
PLUGIN_NAME="./check_rsi.py"

# Check computed RSI period is correct. 

rsiCheck = float(subprocess.check_output([PLUGIN_NAME, "--ticker", TICKER, "--periods", "14", "--raw"]))

if rsiCheck == EXPECTED_RSI:
	print("OK - RSI Calculation of " + str(EXPECTED_RSI) + " correct for ticker " + TICKER)
else:
	print("ERROR - RSI Calculation of " + str(EXPECTED_RSI) + " incorrect for ticker " + TICKER + ", exiting...")
	sys.exit(ERROR)

# No ticker entered.

check_ticker_arg(PLUGIN_NAME)

# Max RSI period.

try:

	rsiMaxCheck = subprocess.check_output([PLUGIN_NAME, "--ticker", TICKER, "--periods", "14", "--max", "50"])
	print("Error, RSI is greater than max, and therefore should have thrown an error, exiting...")
	sys.exit(ERROR)

except subprocess.CalledProcessError as e:

	if "WARNING - RSI(62.95) is above threshold 50" == e.output.rstrip():
		print("OK - RSI max was triggered and threw an error.")
	else:

		print("ERROR - RSI max was not triggered and did not throw an error, exiting...")
		print(e.output)
		sys.exit(ERROR)

# Min RSI period.

try:

	rsiMaxCheck = subprocess.check_output([PLUGIN_NAME, "--ticker", TICKER, "--periods", "14", "--min", "70"])
	print("Error, RSI is less than min, and therefore should have thrown an error, exiting...")
	sys.exit(ERROR)

except subprocess.CalledProcessError as e:

	if "WARNING - RSI(62.95) is below threshold 70" == e.output.rstrip():
		print("OK - RSI min was triggered and threw an error.")
	else:
		print("ERROR - RSI min was not triggered and did not throw an error, exiting...")
		print(e.output)
		sys.exit(ERROR)

########################################################################
# Check Price 

TICKER="CBA"
EXPECTED_PRICE=83.16
PRETTY_PRICE="$83.16 (-1.84%)"
PLUGIN_NAME="./check_price.py"

print("########################################################################")
print("# Check Price Plugin")
print("########################################################################")

# Check raw price is correct. 

priceCheck = float(subprocess.check_output([PLUGIN_NAME, "--ticker", TICKER, "--raw"]))

if priceCheck == EXPECTED_PRICE:
	print("OK - Price check of " + str(EXPECTED_PRICE) + " correct for ticker " + TICKER)
else:
	print("ERROR - price check of " + str(EXPECTED_PRICE) + " incorrect for ticker " + TICKER + ", exiting...")
	sys.exit(ERROR)


# No ticker entered.

check_ticker_arg(PLUGIN_NAME)

# Check pretty price is matches result. 

try:

	subprocess.check_output([PLUGIN_NAME, "--ticker", "CBA"])
	print("Pretty price did not match expected result, and therefore should have thrown an error, exiting...")
	sys.exit(ERROR)

except subprocess.CalledProcessError as e:

	if PRETTY_PRICE == e.output.rstrip():
		print("OK - Pretty price matched expected result: " + "$83.16 (-1.84%)")
	else:

		print("ERROR - Pretty price did not match expected result (" + "$83.16 (-1.84%)" + " ) and something went wrong, exiting...")
		print(e.output)
		sys.exit(ERROR)


########################################################################
# Check SMA 

TICKER="CBA"
EXPECTED_SMA=float(82.99)
PRETTY_PRICE=str("$82.99")
PLUGIN_NAME="./check_sma.py"

print("########################################################################")
print("# Check SMA Plugin")
print("########################################################################")

# Check SMA raw price is correct. 

smaCheck = float(subprocess.check_output([PLUGIN_NAME, "--ticker", TICKER, "--periods", "10", "--raw"]))

if smaCheck == EXPECTED_SMA:
	print("OK - SMA check of " + str(EXPECTED_SMA) + " correct for ticker " + TICKER)
else:
	print("ERROR - SMA check of " + str(EXPECTED_SMA) + " incorrect for ticker " + TICKER + ", should be (" + str(smaCheck) + "), exiting...")
	sys.exit(ERROR)

# No ticker entered.

check_ticker_arg(PLUGIN_NAME)

# Max SMA.

try:

	rsiMaxCheck = subprocess.check_output([PLUGIN_NAME, "--ticker", TICKER, "--periods", "10", "--max", "80"])
	print("Error, Computed SMA result is greater than the threshold, and therefore should have thrown an error, exiting...")
	sys.exit(ERROR)

except subprocess.CalledProcessError as e:

	if "WARNING - SMA($82.99) is above threshold 80" == e.output.rstrip():
		print("OK - SMA max was triggered and threw an error.")
	else:

		print("ERROR - SMA max was not triggered and did not throw an error, exiting...")
		print(e.output)
		sys.exit(ERROR)

# Min SMA.

try:

	rsiMaxCheck = subprocess.check_output([PLUGIN_NAME, "--ticker", TICKER, "--periods", "10", "--min", "90"])
	print("Error, Computed SMA result is below than the threshold, and therefore should have thrown an error, exiting...")
	sys.exit(ERROR)

except subprocess.CalledProcessError as e:

	if "WARNING - SMA($82.99) is below threshold 90" == e.output.rstrip():
		print("OK - SMA min was triggered and threw an error.")
	else:

		print("ERROR - SMA min was not triggered and did not throw an error, exiting...")
		print(e.output)
		sys.exit(ERROR)	

########################################################################
# Check Website 

TICKER="CBA"
UNCHANGING_TEST_URL="http://localhost/unchanging-page.php"
UNCHANGING_TEST_URL_CS="331c2302417570388a988025460ada352dce2bb3f0ae13a9942538b815e59d2c"

PLUGIN_NAME="./check_website.py"


print("########################################################################")
print("# Check Website Plugin")
print("########################################################################")

# Get the checksum of a known (non-dynamic) web-page.
# $./check_website_for_changes.py --url http://192.168.1.179/unchanging-page.php -g
# 331c2302417570388a988025460ada352dce2bb3f0ae13a9942538b815e59d2c

checksum = subprocess.check_output([PLUGIN_NAME, "--url", UNCHANGING_TEST_URL, "-g"])

if not checksum == UNCHANGING_TEST_URL_CS:
	print("Error, Computed checksum result is different than what's expected, exiting...")
	sys.exit(ERROR)
else:
	print("OK - Computed checksum result matches what's expected...")

print("########################################################################")
print("# Smoke tests completed...")
print("########################################################################")
sys.exit(OK)
