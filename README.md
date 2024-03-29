<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/shark_ui_patches/logofullsize.png?raw=true">
</p>

# Shark - An Algorithmic Trading Platform

Shark is an open source algorithmic trading platform under active development.

It enables the use of programmable algorithms to identify and execute upon trading opportunities, perform back/foward testing, comes with a multitude of plugins, and can operate against REST and streaming APIs.

The example configuration demostrates a simple moving average crossover against the TOP 20 Crypto, and though the demo focuses on cryptocurrencies, it could easily be adjusted to suit any financial market.  

See the [plugins](https://github.com/danielneil/Shark-Plugins) for a list of capabilities, and broker configurations can be found [here](https://github.com/danielneil/Shark-Brokers).

See the example [configuration](https://github.com/danielneil/Shark-Config), or the [RSI2 tutorial](https://github.com/danielneil/Shark-Doc/blob/main/tutorials/RSI2.md) to get started.

Please reach out to me on [Linked In!](https://www.linkedin.com/in/danielneilcanb) 

## Instructions 

<details>
<summary>System Requirements</summary>
<br>
  
| Operating System | CPU  | RAM | DISK |
| ------------- | ------------- | ------------- | ------------- |
| Rocky Linux 9.2         | 4 CPU   | 8 GB |80 GB  |
  
</details>


## Quick Setup

<details>
<summary>System Installation</summary>
<br>
  
1. Prepare a vanilla Rocky Linux 9.2 (server instance) with VirtualBox ([help](https://kifarunix.com/install-rocky-linux-9-on-virtualbox/)).

2. Install epel - open a terminal, and run:
  ```
dnf install epel-release -y
```
  
3. Install ansible - open a terminal, and run:
  ```
dnf install ansible -y
```

4. Install git - open a terminal, and run:
  ```
dnf install git -y
```

5. Open a terminal, and run:
```
git clone https://github.com/danielneil/Shark.git && cd Shark && ./build.sh
```
6. Navigate to http://shark-server/shark (web credentials are shark/shark) - it will take a few minutes to populate with data.
</details>


## Trading the TOP 20 Crypto

<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/screenshots/shark-crypto.png?raw=true">
</p>

## Shark Plugins (sma, yahoo_finance, backtest)

See the [plugins](https://github.com/danielneil/Shark-Plugins) for a list of capabilities.

<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/screenshots/shark-plugin-details.jpg?raw=true">
</p>

## Backtesting

<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/screenshots/shark-backtest-plugin.png?raw=true">
</p>

## Backtest Report (custom strategy against BTC-USD)

<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/screenshots/backtest-report.png?raw=true">
</p>
