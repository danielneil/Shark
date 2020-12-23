# AutomatedTradingPlatform

Nagios is known for being a tool to help IT folks monitor IT infrastructure, but with a few tweaks it can be used as an automated trading platform.

This will be a simple proof of concept which turns Nagios Core into a trading platform that enables it to use a strategy to identify and execute upon trading opportunities.

The example strategy is simple moving averages crossover with the chosen financial market being the ASX (top 20 stocks).

I am available for consultation and employment. 

# Setup Instructions

1. Install ansible on your local machine.

2. Prepare a vanilla Debian server which will host the application

3. Add the debian server's IP address to the ./hosts files under [atp-server]

4. Change the http credentials in ./site.yml to your liking.

5. Run: ./build.sh

6. Navigate to https://atp-server/nagios.

# Warning.

Do not build this on an internet-facing server.
