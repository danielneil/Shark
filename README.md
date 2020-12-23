# Automated Trading Platform

Nagios is known for being a tool to help IT folks monitor IT infrastructure, but with a few tweaks it can be used as an automated trading platform.

This is a simple proof of concept which turns Nagios Core into a trading platform that enables it to use a strategy to identify and execute upon trading opportunities.

The example strategy is simple moving averages crossover with the chosen financial market being the ASX (top 20 stocks).

I am available for consultation and employment. 

# Setup Instructions

1. Install ansible on your local machine.

2. Prepare a vanilla Debian server which will host the application

3. Add the debian server's IP address to the ./hosts files under [atp-server]

4. Change the http credentials in ./site.yml to your liking.

5. Run: ./build.sh

6. Navigate to https://atp-server/nagios.

# Screen Shots

## Ticker Status Details For All Ticker Groups

![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)

## Indicator Status Details For All Tickers

![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)

## Service Overview For All Host Groups

![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)

## Ticker Status Details For All Ticker Groups

![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)

# Warning.

Do not build this on an internet-facing server.
