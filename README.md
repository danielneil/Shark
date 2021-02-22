# Shark - An Algorithmic Trading Platform

Shark is an open source algorithmic trading platform derived from tools that monitor IT infrastructure.

It enables the use of programmable strategies to identify and execute upon trading opportunities.

The example strategy is simple moving averages crossover with the chosen financial market being the Australian Stock Exchange (Top 20). It also demonstrates determing the strength of an opportunity using the RSI indicator coupled with an automatic backtest.  

Though it focuses on the ASX, it could easily be adjusted to suit any financial market, along with an adapted strategy.  

The ticker data supplied doesn't refresh. If you need it to refresh, see my other project that uses [Nifi](https://github.com/danielneil/Using-NiFi-on-Yahoo-Finance).

See the [plugins](https://github.com/danielneil/Shark/blob/main/doc/README.PLUGINS.md) for a list of capabilities.

See the example [strategy](https://github.com/danielneil/Shark/blob/main/automatedtradingplatform/files/strategies/moving_averages.py), along with the correlating [backtest](https://github.com/danielneil/Shark/blob/main/automatedtradingplatform/files/strategies/backtesting/backtest_moving_averages.py).

# Setup Instructions

1. Install ansible on your local machine.

2. Prepare a vanilla Debian server.

3. Add its IP address to the ./hosts files under [shark-server]

4. Change the http credentials in ./site.yml to your liking.

5. Run: 
```
git clone https://github.com/danielneil/Shark.git && cd Shark && ./build.sh
```
6. Navigate to https://shark-server/nagios using the aforementioned credentials.

# Screen Shots

![alt text](https://github.com/danielneil/Shark/blob/main/screenshots/screenshot.JPG?raw=true)
![alt text](https://github.com/danielneil/Shark/blob/main/screenshots/opportunity.JPG?raw=true)
![alt text](https://github.com/danielneil/Shark/blob/main/screenshots/backtest.JPG?raw=true)

# Warning

1. Don't install this on an internet-facing server.

2. [Read the disclaimer](https://github.com/danielneil/Shark/blob/main/DISCLAIMER).

