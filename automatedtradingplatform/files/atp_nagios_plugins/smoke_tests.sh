#!/bin/bash 

# Check RSI

if [ `./check_rsi.py --ticker CBA --rsi 14` == 62.95 ]; 
then
	echo 'Computed RSI is correct'
else
	echo 'Computed RSI is incorrect'
	exit 1
fi
