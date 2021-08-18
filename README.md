<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/ui_patches/logofullsize.png?raw=true">
</p>

# Shark - An Algorithmic Trading Platform

Shark is an open source algorithmic trading and back/forward testing platform that is under active development.

It enables the use of (simultaneous) programmable algorithms to identify and execute upon trading opportunities, that can be coupled with a multitude of plugins, and also includes an embedded development environment. 

The example configuration demostrates a simple moving averages crossover against the Crypto TOP 20, and though the demo focuses on cryptocurrencies, it could easily be adjusted to suit any financial market.  

See the example [backtest](https://github.com/danielneil/Shark/blob/main/shark/files/strategies/backtesting/backtest_moving_averages.py), and [configuration](https://github.com/danielneil/Shark-Config) to get started.

See the [plugins](https://github.com/danielneil/Shark/blob/main/doc/README.PLUGINS.md) for a list of capabilities.

# Instructions 

<details>
<summary>System Requirements</summary>
<br>
  
| Operating System | CPU  | RAM | DISK |
| ------------- | ------------- | ------------- | ------------- |
| Rocky Linux 8+         | 4 CPU   | 4 GB | 80 GB  |
  
</details>


## Setup

<details>
<summary>System Installation</summary>
<br>
  
1. Prepare a vanilla Rocky Server with VirtualBox ([help](https://kifarunix.com/install-rocky-linux-8-on-virtualbox/)).

2. Install ansible ([help](https://www.how2shout.com/linux/how-to-install-ansible-on-rocky-linux-8-or-almalinux/)).

3. Install Git ([help](https://tastethelinux.com/2021/08/06/how-to-install-git-on-rocky-linux-8-ec2-aws/)).

4. Open a terminal, and run:
```
git clone https://github.com/danielneil/Shark.git && cd Shark && ./build.sh
```
5. Navigate to http://debian-server-ip/nagios (web credentials are shark/shark).

  
</details>


# Screenshots

<table>
 <tr>
   <td style="font-weight: bold">Instrument List</td>
  <td> <img width="300" src="https://github.com/danielneil/Shark/blob/main/screenshots/screenshot.JPG?raw=true">
  <td style='font-weight: bold'>Sorting by Instrument Groups
  <td> <img width="300" src="https://github.com/danielneil/Shark/blob/main/screenshots/industry-groups-view.JPG?raw=true" />
  <tr>
   <td style='font-weight: bold'>Sorting by Plugin Groups
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

Shark has lots of moving parts, so feel free to cherry pick a component that interests you, and go nuts.

Visit us on [Reddit](https://www.reddit.com/r/shark)!
