<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/ui_patches/logofullsize.png?raw=true">
</p>

# Shark - An Algorithmic Trading Platform

Shark is scalable open source algorithmic trading and backtesting platform.

It enables the use of (simultaneous) programmable strategies to identify and execute upon trading opportunities, coupled with integrated backtesting. 

The example strategy is simple moving averages crossover against the Australian Stock Exchange's S&P/ASX 20. It also demonstrates determing the strength of an opportunity using the RSI indicator accompanied with a historical backtest.  

Though this example focuses on the ASX, it could easily be adjusted to suit any financial market, along with an adapted strategy and backtest.  

The ticker data supplied doesn't refresh (nor is it ''fresh''). If you need it to refresh, see my other project, [Mako](https://github.com/danielneil/Mako), which uses Nifi to synchronise financial data from various sources.

See the [plugins](https://github.com/danielneil/Shark/blob/main/doc/README.PLUGINS.md) for a list of capabilities.

See the example [strategy](https://github.com/danielneil/Shark/blob/main/shark/files/strategies/moving_averages.py), along with the correlating [backtest](https://github.com/danielneil/Shark/blob/main/shark/files/strategies/backtesting/backtest_moving_averages.py).

# Instructions 

<details>
<summary>System Requirements</summary>
<br>
  
| Operating System | CPU  | RAM | DISK |
| ------------- | ------------- | ------------- | ------------- |
| Debian GNU/Linux 10         | 4 CPU   | 8 GB | 80 GB  |
  
</details>


## Setup

<details>
<summary>System Installation</summary>
<br>
  
1. Prepare a vanilla Debian Server with VirtualBox ([help](https://linuxhint.com/install_debian10_virtualbox/)).

2. Install ansible ([help](https://linuxhint.com/install_ansible_debian10/)).

3. Install Git ([help](https://linuxhint.com/install_git_debian_10/)).

4. Open a terminal, and run:
```
git clone https://github.com/danielneil/Shark.git && cd Shark && ./build.sh
```
5. Navigate to http://debian-server-ip/nagios (web credentials are shark/shark).

  
</details>


# Screenshots

<table>
 <tr>
   <td style="font-weight: bold">Ticker List</td>
  <td> <img width="300" src="https://github.com/danielneil/Shark/blob/main/screenshots/screenshot.JPG?raw=true">
  <td style='font-weight: bold'>Sorting by Industry Groups
  <td> <img width="300" src="https://github.com/danielneil/Shark/blob/main/screenshots/industry-groups-view.JPG?raw=true" />
  <tr>
   <td style='font-weight: bold'>Sorting by Indicator Groups
   <td> <img width="300" src="https://github.com/danielneil/Shark/blob/main/screenshots/indicator-groups.JPG?raw=true" />
   <td style='font-weight: bold'>Opportunity Detection
   <td> <img width="300" src="https://github.com/danielneil/Shark/blob/main/screenshots/strategy.JPG?raw=true"/>
   <tr>
    <td>Integrated Backtesting
    <td> <img width="300" src="https://github.com/danielneil/Shark/blob/main/screenshots/backtest.JPG?raw=true" />
    <td>Historic Strategy Performance (Backtest) 
    <td> <img width="300" src="https://github.com/danielneil/Shark/blob/main/screenshots/strategy-performance.JPG?raw=true"/>
</table>

# Contributing 

Shark has lots of moving parts, so feel free to cherry pick a component that interests you, and send me a pull request.
    
# I am looking for a sponsor
     
I am looking for a sponsor to continue work on this project, if you are interested, please contact me.  
