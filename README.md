<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/ui_patches/logofullsize.png?raw=true">
</p>

# Shark - An Algorithmic Trading Platform

Shark is an open source algorithmic trading and back/forward testing platform under active development.

It enables the use of (simultaneous) programmable algorithms to identify and execute upon trading opportunities, that can be coupled with a multitude of plugins.

The example configuration demostrates a simple moving averages crossover against the Crypto TOP 20, and though the demo focuses on cryptocurrencies, it could easily be adjusted to suit any financial market.  

See the example [configuration](https://github.com/danielneil/Shark-Config) to get started.

See the [plugins](https://github.com/danielneil/Shark/blob/main/doc/README.PLUGINS.md) for a list of capabilities.

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

2. Install ansible ([help](https://www.how2shout.com/linux/how-to-install-ansible-on-rocky-linux-8-or-almalinux/)).

3. Install Git ([help](https://tastethelinux.com/2021/08/06/how-to-install-git-on-rocky-linux-8-ec2-aws/)).

4. Open a terminal, and run:
```
git clone https://github.com/danielneil/Shark.git && cd Shark && ./build.sh
```
5. Navigate to http://debian-server-ip/nagios (web credentials are shark/shark).

  
</details>


## Screenshot



## Contributing 

Visit us on [Reddit](https://www.reddit.com/r/shark)!
