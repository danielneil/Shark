#!/usr/bin/python

import subprocess
import sys

ERROR= 1
OK= 0

TICKER="CBA"

########################
# Check RSI Plugin

TICKER="CBA"
EXPECTED_RSI=62.95

print("Running check_rsi.py checks....")

rsiCheck = float(subprocess.check_output(["/atp/nagios_plugins/check_rsi.py", "--ticker", TICKER, "--rsiPeriod", "14"]))

if rsiCheck == EXPECTED_RSI:
	print("RSI Calculation of " + EXPECTED_RSI + " correct for ticker " + TICKER)
else:
	print("RSI Calculation of " + EXPECTED_RSI + " incorrect for ticker " + TICKER)
	sys.exit(ERROR)