<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/shark_ui_patches/logofullsize.png?raw=true">
</p>

# Shark - An Algorithmic Trading Platform

Shark is an open source algorithmic trading platform under active development.

It enables the use of (simultaneous) programmable algorithms to identify and execute upon trading opportunities, perform back/foward testing, and comes with a multitude of plugins.

The example configuration demostrates a simple moving averages crossover against the Crypto TOP 20, and though the demo focuses on cryptocurrencies, it could easily be adjusted to suit any financial market.  

See the example [configuration](https://github.com/danielneil/Shark-Config) to get started.

## Instructions 

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
  
1. Prepare a vanilla Rocky Linux (server instance) with VirtualBox ([help](https://kifarunix.com/install-rocky-linux-8-on-virtualbox/)).

2. Install epel ([help](https://www.how2shout.com/linux/how-to-enable-epel-repository-on-rocky-linux-8)).
  
3. Install ansible ([help](https://www.how2shout.com/linux/how-to-install-ansible-on-rocky-linux-8-or-almalinux/)).

4. Install Git ([help](https://tastethelinux.com/2021/08/06/how-to-install-git-on-rocky-linux-8-ec2-aws/)).

5. Open a terminal, and run:
```
git clone https://github.com/danielneil/Shark.git && cd Shark && ./build.sh
```
6. Navigate to http://shark-server/nagios (web credentials are shark/shark).
</details>


## Screenshot - Crypto TOP 20

<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/screenshots/shark-crypto.png?raw=true">
</p>

## Contributing 

Visit us on [Reddit](https://www.reddit.com/r/shark)!
