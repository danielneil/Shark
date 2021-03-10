# Plugins Documentation

This is the plugins documentation.

The plugins enable the platform to monitor and alert on just about **anything** of interest; if its online, it can be monitored.

# Contents
* [check_rsi](#check_rsi)
* [check_strategy](#check_strategy)
* [check_price](#check_price)
* [check_sma](#check_sma)
* [check_website_for_changes](#check_website_for_changes)
* [check_vix](#check_vix)
* [check_backtest](#check_backtest)
* [check_ema](#check_ema)
* [check_trend](#check_trend)
* [check_short_interest](#check_short_interest)
## <a name="check_rsi"/>check_rsi

**Usage:** check_rsi.py [-h] [-t TICKER] [-p PERIODS] [-max MAX] [-min MIN]
                    [-r [RAW]]

This plugin checks the relative strength index (RSI) for a stock. Based on the
output, you can decide to set certain warning and critical threshold levels.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        ticker code of the stock
  -p PERIODS, --periods PERIODS
                        Number of trading periods for which to compute
                        against.
  -max MAX, --max MAX   Warn if the RSI is greater than this threshold.
  -min MIN, --min MIN   Warn if the RSI is less than this threshold.
  -r [RAW], --raw [RAW]
                        Just print the price minus pretty output.
## <a name="check_strategy"/>check_strategy

**Usage:** check_strategy.py [-h] [-t TICKER] [-s STRATEGY]

This executes the strategy code. For a simple strategy, see the template for
an example

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock in question
  -s STRATEGY, --strategy STRATEGY
                        The file name of the custom strategy
## <a name="check_price"/>check_price

**Usage:** check_price.py [-h] [-t TICKER] [-r [RAW]]

This plugin checks the price for a stock. Based on the output, you can decide
to set certain warning and critical threshold levels.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock
  -r [RAW], --raw [RAW]
                        Just print the price minus pretty output and return
                        OK(0)
## <a name="check_sma"/>check_sma

**Usage:** check_sma.py [-h] [-t TICKER] [-p PERIODS] [-r [RAW]] [-max MAX]
                    [-min MIN]

This plugin checks the simple moving average (SMA) for a stock. Based on the
output, you can decide to set certain warning and critical threshold levels.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock.
  -p PERIODS, --periods PERIODS
                        Number of trading periods for which to compute
                        against.
  -r [RAW], --raw [RAW]
                        Just print the price minus pretty output.
  -max MAX, --max MAX   Warn if the result is greater than this threshold.
  -min MIN, --min MIN   Warn if the result is less than this threshold.
## <a name="check_website_for_changes"/>check_website_for_changes

**Usage:** check_website_for_changes.py [-h] [-u URL] [-c CHECKSUM]
                                    [-l IGNORELINE] [-g [GENERATE]]
                                    [-s [SCREENSHOT]]

This plugin monitors a website of interest for changes. E.g. the investors
section of a publicly listed company's website. By default, it performs a
SHA256 of the website's source code. It can ignore specific lines to overcome
a website which may generate dynamic content upon each load. For more complex
websites, the plugin can compare checksums of screenshots for webpages.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL of the website of interest.
  -c CHECKSUM, --checksum CHECKSUM
                        The expected checksum, alarms if mismatch.
  -l IGNORELINE, --ignoreLine IGNORELINE
                        Ignore a specific line of the returned source code (
  -g [GENERATE], --generate [GENERATE]
                        Get the checksum for a specific website. Used to
                        create/refresh checksums
  -s [SCREENSHOT], --screenshot [SCREENSHOT]
                        Instead of diffing the source code of a webpage
                        (default), use a checksum of a screenshot instead
## <a name="check_vix"/>check_vix

**Usage:** check_vix.py [-h]

This plugin checks the VIX (Volatility Index) for a stock. Based on the
output, you can decide to set certain warning and critical threshold levels.

**Optional Arguments**:
  -h, --help  show this help message and exit
## <a name="check_backtest"/>check_backtest

**Usage:** check_backtest.py [-h] [-t TICKER] [-b BACKTEST] [-s SHARES]
                         [-c CAPITAL] [-n]

This executes the backtest code. For a simple backtest example, see the
template

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock in question
  -b BACKTEST, --backtest BACKTEST
                        The file name of the backtest
  -s SHARES, --shares SHARES
                        The imaginary number of shares to use in the backtest
  -c CAPITAL, --capital CAPITAL
                        The imaginary amount of a capital which to use in the
                        backtest
  -n, --noreport        Do not generate the back test reports
## <a name="check_ema"/>check_ema

**Usage:** check_ema.py [-h] [-t TICKER] [-p PERIODS] [-r [RAW]] [-max MAX]
                    [-min MIN]

This plugin checks the exponential moving average (EMA) for a stock. Based on
the output, you can decide to set certain warning and critical threshold
levels.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock.
  -p PERIODS, --periods PERIODS
                        Number of trading periods for which to compute
                        against.
  -r [RAW], --raw [RAW]
                        Just print the price minus pretty output.
  -max MAX, --max MAX   Warn if the result is greater than this threshold.
  -min MIN, --min MIN   Warn if the result is less than this threshold.
## <a name="check_trend"/>check_trend

**Usage:** check_trend.py [-h] [-t TICKER] [-1st FIRSTMA] [-2nd SECONDMA]
                      [-3rd THIRDMA]

This plugin checks the trend for a stock. Based on the output, you can decide
to set certain warning and critical threshold levels.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock
  -1st FIRSTMA, --firstMA FIRSTMA
                        First moving average (the shorter, e.g. 10 days)
  -2nd SECONDMA, --secondMA SECONDMA
                        Second moving average (the longer, e.g. 50 days)
  -3rd THIRDMA, --thirdMA THIRDMA
                        Third moving average (the longest. e.g. 100 days)
## <a name="check_short_interest"/>check_short_interest

**Usage:** check_short_interest.py [-h] [-t TICKER]

This plugin checks the short interest for a stock. Based on the output, you
can decide to set certain warning and critical threshold levels.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock


This is automatically generated, do not edit this file, instead amend the help text in the plugin's source code.
