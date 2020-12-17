# AutomatedTradingPlatform

##########################################
# PROJECT STATUS: UNDER ACTIVE DEVELOPMENT
##########################################

Nagios is known for being a tool to help IT folks monitor IT infrastructure, but with a few tweaks it can be used as an automated trading platform.

This is a simple proof of concept which turns Nagios Core into a full blown trading platform that enables it to use a strategy to identify and execute upon trading opportunities.

The example strategy is simple mean reversion, coupled with shorts analysis, backtesting, and the chosen financial market is the ASX.

Back testing and technical indicators are derived from Yahoo Finance data, so you will need to download these for each instrument you desire.

I am available for consultation and employment. 

# Setup Instuctions

1. Install ansible on your local machine.

2. Prepare a vanilla Debian server which will host the application

3. Add the debian server's IP address to the ./hosts files under [atp-server]

4. Change the http credentials in ./site.yml to your liking.

5. Run: ./build.sh

6. Navigate to https://atp-server/nagios.

# Warning.

Do not build this on an internet-facing server.
