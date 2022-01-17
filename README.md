<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/shark_ui_patches/logofullsize.png?raw=true">
</p>

# Shark - An Algorithmic Trading Platform

Shark is an open source algorithmic trading platform under active development.

It enables the use of (simultaneous) programmable algorithms to identify and execute upon trading opportunities, perform back/foward testing, comes with a multitude of plugins, and can operate with REST and streaming APIs.

The example configuration demostrates a simple moving average crossover against the TOP 20 Crypto, and though the demo focuses on cryptocurrencies, it could easily be adjusted to suit any financial market.  

See the [plugins](https://github.com/danielneil/Shark-Plugins) for a list of capabilities, and broker configurations can be found [here](https://github.com/danielneil/Shark-Brokers).

See the example [configuration](https://github.com/danielneil/Shark-Config) to get started.

## Instructions 

<details>
<summary>System Requirements</summary>
<br>
  
| Operating System | CPU  | RAM | DISK |
| ------------- | ------------- | ------------- | ------------- |
| Rocky Linux 8+         | 4 CPU   | 8 GB |80 GB  |
  
</details>


## Setup

<details>
<summary>System Installation</summary>
<br>
  
1. Prepare a vanilla Rocky Linux (server instance) with VirtualBox ([help](https://kifarunix.com/install-rocky-linux-8-on-virtualbox/)).

2. Install epel - open a terminal, and run:
  ```
yum install epel-release -y
```
  
3. Install ansible - open a terminal, and run:
  ```
yum install ansible -y
```

4. Install git - open a terminal, and run:
  ```
yum install git -y
```

5. Open a terminal, and run:
```
git clone https://github.com/danielneil/Shark.git && cd Shark && ./build.sh
```
6. Navigate to http://shark-server/nagios (web credentials are shark/shark) - it will take about 5 mins to populate.
</details>


## Screenshot - Trading the TOP 20 Crypto

<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/screenshots/shark-crypto.png?raw=true">
</p>

## Screenshot - Plugins

<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/screenshots/shark-plugin-details.jpg?raw=true">
</p>

## Screenshot - Backtest Report

<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/screenshots/backtest-report.png?raw=true">
</p>


## Video - Installing Shark on Rocky Linux 8

[![asciicast](https://asciinema.org/a/460006.svg)](https://asciinema.org/a/460006)

## Contributing 

Need help? Visit us on [Reddit](https://www.reddit.com/r/shark)!
