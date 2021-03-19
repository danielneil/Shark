<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/algorithmictradingplatform/files/ui_patches/logofullsize.png?raw=true">
</p>

# Shark - An Algorithmic Trading Platform

Shark is scalable open source algorithmic trading platform derived from tools that monitor IT infrastructure.

It enables the use of programmable strategies to identify and execute upon trading opportunities, and also has an integrated backtesting component. 

The example strategy is simple moving averages crossover with the chosen financial market being the Australian Stock Exchange (Top 20 by market cap). It also demonstrates determing the strength of an opportunity using the RSI indicator coupled with a backtest.  

Though this example focuses on the ASX, it could easily be adjusted to suit any financial market, along with an adapted strategy and backtest.  

The ticker data supplied doesn't refresh (nor is it ''fresh''). If you need it to refresh, see my other project that uses [Nifi](https://github.com/danielneil/Using-NiFi-on-Yahoo-Finance).

See the [plugins](https://github.com/danielneil/Shark/blob/main/doc/README.PLUGINS.md) for a list of capabilities.

See the example [strategy](https://github.com/danielneil/Shark/blob/main/algorithmictradingplatform/files/strategies/moving_averages.py), along with the correlating [backtest](https://github.com/danielneil/Shark/blob/main/algorithmictradingplatform/files/strategies/backtesting/backtest_moving_averages.py).

# Setup Instructions

1. Prepare a vanilla Debian Server with VirtualBox ([help](https://linuxhint.com/install_debian10_virtualbox/)).

2. Install ansible ([help](https://linuxhint.com/install_ansible_debian10/)).

3. Install Git ([help](https://linuxhint.com/install_git_debian_10/)).

4. Open a terminal, and run:
```
git clone https://github.com/danielneil/Shark.git && cd Shark && ./build.sh

# The build takes about 5 mins.
```
5. Navigate to https://debian-server-ip/nagios (web credentials are shark/shark).

6. Please reach out to me for help if you get stuck!

# Screenshots

### Main Screen

![Main Screen](https://github.com/danielneil/Shark/blob/main/screenshots/screenshot.JPG?raw=true)

### Sorting by Industry Groups

![Main Screen](https://github.com/danielneil/Shark/blob/main/screenshots/industry-groups-view.JPG?raw=true)

### Sorting by Indicator Groups

![Main Screen](https://github.com/danielneil/Shark/blob/main/screenshots/indicator-groups.JPG?raw=true)

### Opportunity Detection

![Main Screen](https://github.com/danielneil/Shark/blob/main/screenshots/strategy.JPG?raw=true)

### Backtest Alerting

![Main Screen](https://github.com/danielneil/Shark/blob/main/screenshots/backtest.JPG?raw=true)

### Historic Strategy Performance

![Main Screen](https://github.com/danielneil/Shark/blob/main/screenshots/strategy-performance.JPG?raw=true)

### Historic Strategy Performance - Transaction Log 

![Main Screen](https://github.com/danielneil/Shark/blob/main/screenshots/strategy-transactions-log.JPG?raw=true)

# Want to get involved? 

Shark has lots of moving parts, so feel free to cherry pick a component that interests you.

The technology stack comprises of the below, therefore knowledge of ( or a willingness to learn ) **any** of the following would be highly warranted.

### Programming

Bash Scripting, Ansible, C/C++, BOOST, HTML/CSS, PHP, SQL, CatBoost, JSON, CSV, Python, PANDAS, REST and PERL

### Technologies

Linux (ideally Debian or a derivative), the Nagios tech stack (Nagios Core / Plugins / NRPE), RabbitMQ, Redis, PyAlgoTrade, Elasticsearch, Logtstash, Apache ZooKeeper, Apache Drill, Apache HTTPD, Apache NiFi and Docker.

### Financials

An understanding of financial markets, algorithmic trading, or any kind of analytical specialisations are **strongly** desired. 

### Mathematics

Any kind of mathematical knowledge in relation to financial algorithms is **strongly** desired. 

# Warning

1. Don't install this on an internet-facing server.

2. [Read the disclaimer](https://github.com/danielneil/Shark/blob/main/DISCLAIMER).

