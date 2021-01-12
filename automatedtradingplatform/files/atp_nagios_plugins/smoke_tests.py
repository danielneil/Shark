#!/usr/bin/python

import subprocess
import sys

ERROR= 1
OK= 0

TICKER="CBA"

########################################################################
# Check RSI Plugin

TICKER="CBA"
EXPECTED_RSI=62.95

print("########################################################################")
print("# Check RSI Plugin\n")

# Check computed RSI period is correct. 

rsiCheck = float(subprocess.check_output(["/atp/nagios_plugins/check_rsi.py", "--ticker", TICKER, "--rsiPeriod", "14"]))

if rsiCheck == EXPECTED_RSI:
	print("OK - RSI Calculation of " + str(EXPECTED_RSI) + " correct for ticker " + TICKER)
else:
	print("ERROR - RSI Calculation of " + str(EXPECTED_RSI) + " incorrect for ticker " + TICKER + ", exiting...")
	sys.exit(ERROR)

# No ticker entered.

try:

	rsiCheck = float(subprocess.check_output(["/atp/nagios_plugins/check_rsi.py"]))
	print("Error, a ticker was not supplied, and therefore should have thrown an error, exiting...")
	sys.exit(ERROR)

except subprocess.CalledProcessError as e:

	if "UNKNOWN - No ticker found" == e.output.rstrip():
		print("OK - a ticker was not supplied and threw an error.")
	else:

		print("ERROR - a ticker was not supplied and something went wrong, exiting...")
		print(e.output)
		sys.exit(ERROR)

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