#!/usr/bin/python

import subprocess
import sys

ERROR= 1
OK= 0

########################################################################
# Ticker Arg check
def check_ticker_arg(check_plugin):
	try:

		rsiCheck = float(subprocess.check_output(["/atp/nagios_plugins/" + check_plugin]))
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
PLUGIN_NAME="check_rsi.py"

# Check computed RSI period is correct. 

rsiCheck = float(subprocess.check_output(["/atp/nagios_plugins/check_rsi.py", "--ticker", TICKER, "--rsiPeriod", "14"]))

if rsiCheck == EXPECTED_RSI:
	print("OK - RSI Calculation of " + str(EXPECTED_RSI) + " correct for ticker " + TICKER)
else:
	print("ERROR - RSI Calculation of " + str(EXPECTED_RSI) + " incorrect for ticker " + TICKER + ", exiting...")
	sys.exit(ERROR)

# No ticker entered.

check_ticker_arg(PLUGIN_NAME)

# Max RSI period.

try:

	rsiMaxCheck = subprocess.check_output(["/atp/nagios_plugins/check_rsi.py", "--ticker", TICKER, "--rsiPeriod", "14", "--max", "50"])
	print("Error, RSI is greater than max, and therefore should have thrown an error, exiting...")
	sys.exit(ERROR)

except subprocess.CalledProcessError as e:

	if "WARNING - RSI(62.95) is above 50" == e.output.rstrip():
		print("OK - RSI max was triggered and threw an error.")
	else:

		print("ERROR - RSI max was not triggered and did not throw an error, exiting...")
		print(e.output)
		sys.exit(ERROR)

# Min RSI period.

try:

	rsiMaxCheck = subprocess.check_output(["/atp/nagios_plugins/check_rsi.py", "--ticker", TICKER, "--rsiPeriod", "14", "--min", "70"])
	print("Error, RSI is less than min, and therefore should have thrown an error, exiting...")
	sys.exit(ERROR)

except subprocess.CalledProcessError as e:

	if "WARNING - RSI(62.95) is below 70" == e.output.rstrip():
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
PLUGIN_NAME="check_price.py"

print("########################################################################")
print("# Check Price Plugin")
print("########################################################################")

# Check raw price is correct. 

priceCheck = float(subprocess.check_output(["/atp/nagios_plugins/check_price.py", "--ticker", TICKER, "--raw"]))

if priceCheck == EXPECTED_PRICE:
	print("OK - Price check of " + str(EXPECTED_PRICE) + " correct for ticker " + TICKER)
else:
	print("ERROR - price check of " + str(EXPECTED_PRICE) + " incorrect for ticker " + TICKER + ", exiting...")
	sys.exit(ERROR)


# No ticker entered.

check_ticker_arg(PLUGIN_NAME)

# Check pretty price is matches result. 

try:

	subprocess.check_output(["/atp/nagios_plugins/check_price.py", "--ticker", "CBA"])
	print("Pretty price did not match expected result, and therefore should have thrown an error, exiting...")
	sys.exit(ERROR)

except subprocess.CalledProcessError as e:

	if PRETTY_PRICE == e.output.rstrip():
		print("OK - Pretty price matched expected result: " + "$83.16 (-1.84%)")
	else:

		print("ERROR - Pretty price did not match expected result (" + "$83.16 (-1.84%)" + " ) and something went wrong, exiting...")
		print(e.output)
		sys.exit(ERROR)