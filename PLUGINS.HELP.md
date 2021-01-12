# Documentation for Plugins
## automatedtradingplatform/files/nagios_plugins/check_rsi.py

usage: check_rsi.py [-h] [-t TICKER] [-r RSIPERIOD] [-max MAXRSI]
                    [-min MINRSI]

This plugin computes the relative strength index (RSI) for a stock.

optional arguments:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        ticker code of the stock
  -r RSIPERIOD, --rsiPeriod RSIPERIOD
                        RSI period of which to base the calculation upon.
  -max MAXRSI, --maxRSI MAXRSI
                        Warn if the RSI is greater than this threshold.
  -min MINRSI, --minRSI MINRSI
                        Warn if the RSI is less than this threshold.

## automatedtradingplatform/files/nagios_plugins/check_template.py

usage: check_template.py [-h] [-t TICKER]

This is a template for a python check for the trading platform, make it as
descriptive as possible as it will be used to generate documentation

optional arguments:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        ticker code of the stock

## automatedtradingplatform/files/nagios_plugins/check_strategy.py

usage: check_strategy.py [-h] [-t TICKER] [-s STRATEGY]

This script calls the strategy the strategy defined in the nagios
configuration. Do not make changes here. See the template strategy for an
example

optional arguments:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock in question
  -s STRATEGY, --strategy STRATEGY
                        The file name of the custom strategy

## automatedtradingplatform/files/nagios_plugins/check_price.py

usage: check_price.py [-h] [-t TICKER] [-r [RAW]]

Get the latest price of a stock.

optional arguments:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock
  -r [RAW], --raw [RAW]
                        Just print the price minus pretty output and return
                        OK(0)

## automatedtradingplatform/files/nagios_plugins/check_website.py

usage: check_website.py [-h] [-t TICKER] [-u URL]

This plugin monitors a website for changes. E.g. the Investor Information
section of a publicly listed company, or a page displaying news for a specific
derivative.

optional arguments:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        ticker code of the stock
  -u URL, --url URL     URL of the website of interest

## automatedtradingplatform/files/nagios_plugins/check_sma.py

usage: check_sma.py [-h] [-t TICKER] [-d DAYS] [-r [RAW]]

Computes a simple moving average of a specific ASX ticker against a specific
number of days.

optional arguments:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock.
  -d DAYS, --days DAYS  Number of days for which to compute the SMA against.
  -r [RAW], --raw [RAW]
                        Just print the price minus pretty output and return
                        OK(0)

## automatedtradingplatform/files/nagios_plugins/check_vix.py

13.9

## automatedtradingplatform/files/nagios_plugins/check_trend.py

usage: check_trend.py [-h] [-t TICKER] [-1st FIRSTMA] [-2nd SECONDMA]
                      [-3rd THIRDMA]

This analyses the trend of a stock based upon multiple moving averages. It
takes three numbers/moving averages and determines if the stock is in an
uptrend, and also returns a range calculation to determine the 'distance'
between the moving averages

optional arguments:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock
  -1st FIRSTMA, --firstMA FIRSTMA
                        First moving average (the shorter, e.g. 10 days)
  -2nd SECONDMA, --secondMA SECONDMA
                        Second moving average (the longer, e.g. 50 days)
  -3rd THIRDMA, --thirdMA THIRDMA
                        Third moving average (the longest. e.g. 100 days)

## automatedtradingplatform/files/nagios_plugins/check_short_interest.py

usage: check_short_interest.py [-h] [-t TICKER]

Alarms on the short interest of a specific ASX ticker.

optional arguments:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock

