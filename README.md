# Shark - An Algorithmic Trading Platform

Shark is scalable open source algorithmic trading platform derived from tools that monitor IT infrastructure.

It enables the use of programmable strategies to identify and execute upon trading opportunities.

The example strategy is simple moving averages crossover with the chosen financial market being the Australian Stock Exchange (Top 20 by market cap). It also demonstrates determing the strength of an opportunity using the RSI indicator coupled with a backtest.  

Though it focuses on the ASX, it could easily be adjusted to suit any financial market, along with an adapted strategy.  

The ticker data supplied doesn't refresh. If you need it to refresh, see my other project that uses [Nifi](https://github.com/danielneil/Using-NiFi-on-Yahoo-Finance).

See the [plugins](https://github.com/danielneil/Shark/blob/main/doc/README.PLUGINS.md) for a list of capabilities.

See the example [strategy](https://github.com/danielneil/Shark/blob/main/algorithmictradingplatform/files/strategies/moving_averages.py), along with the correlating [backtest](https://github.com/danielneil/Shark/blob/main/algorithmictradingplatform/files/strategies/backtesting/backtest_moving_averages.py).

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

# Want to get involved? 

Shark's technology stack comprises of the below, therefore I need people with knowledge of ( or a willingness to learn ) any of the following. 

# Programming Languages

Bash Scripting
Ansible
C/C++ 
BOOST
HTML/CSS
PHP
Python 
PANDAS
PERL

# Technologies 

Nagios 
Nagios Plugins
Apache ZooKeeper
Apache Drill
Logtstash
Apache HTTPD
Docker

## Operating Systems

Debian (or a derivative) 

## Financial Analytics

At least an elementry understanding of financial markets and algorithmic trading. 


# Warning

1. Don't install this on an internet-facing server.

2. [Read the disclaimer](https://github.com/danielneil/Shark/blob/main/DISCLAIMER).

