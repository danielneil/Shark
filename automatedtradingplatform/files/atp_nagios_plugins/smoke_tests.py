#!/usr/bin/python

import subprocess
import sys

ERROR= 1
OK= 0

########################
# Check RSI Plugin

rsiCheck = float(subprocess.check_output(["/atp/nagios_plugins/check_rsi.py", "--ticker", "CBA", "--rsiPeriod", "14"]))

if rsiCheck == 62.95:
	print("RSI Calculation correct")
else:
	print("RSI Calculation incorrect, exiting...")
	sys.exit(ERROR)
 


