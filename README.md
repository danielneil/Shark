# Automated Trading Platform

Nagios is known for being a tool to monitor IT infrastructure, but with a few tweaks it can be used to monitor the stock market, and function as an automated trading platform. 

This is a proof of concept which turns Nagios Core into a trading platform that enables it to use a strategy to identify and execute upon trading opportunities.

The example strategy is simple moving averages crossover with the chosen financial market being the Australian Stock Exchange (Top 20).

I am available for consultation and employment. 

# Setup Instructions

1. Install ansible on your local machine.

2. Prepare a vanilla Debian-ish server.

3. Add the Debian server's IP address to the ./hosts files under [atp-server]

4. Change the http credentials in ./site.yml to your liking.

5. Run: ./build.sh

6. Navigate to https://atp-server/nagios using the aforementioned credentials.

# Screen Shots

### Stock Status Details For All Stock Groups

![alt text](https://github.com/danielneil/AutomatedTradingPlatform/blob/main/screenshots/ticker-status.JPG?raw=true)

### Indicator Status Details For All Stocks

![alt text](https://github.com/danielneil/AutomatedTradingPlatform/blob/main/screenshots/indicator-status-all-stocks.JPG?raw=true)

### Indicator Overview For All Stock Groups

![alt text](https://github.com/danielneil/AutomatedTradingPlatform/blob/main/screenshots/indicator-overview.JPG?raw=true)

### Detection of a Trading Opportunity 

![alt text](https://github.com/danielneil/AutomatedTradingPlatform/blob/main/screenshots/trading-strategy-detected.JPG?raw=true)

# Warning

1. Don't install this on an internet-facing server.

2. [Read the disclaimer](https://github.com/danielneil/AutomatedTradingPlatform/blob/main/DISCLAIMER)

