#!/usr/bin/bash

if ! `which figlet &> /dev/null` ; then
  dnf install figlet -y &> /dev/null
fi

if ! `which jp2a &> /dev/null` ; then
 dnf install -y https://tchung.org/jp2a/files/jp2a-1.0.8-1.el8.x86_64.rpm &> /dev/null
fi

git pull &> /dev/null

/usr/bin/figlet Shark
printf "The Algorithmic Trading Platform..."
printf "\nAuthor: danielneil"
jp2a shark/files/screenshots/shark.jpg --background=light

printf "\n\nInstalling Shark..."
ansible-playbook ./site.yml -i hosts --ssh-extra-args='-o ServerAliveInterval=3600'

printf "\n\nInstalling Shark Plugins..."
ansible-playbook /shark/Shark-Plugins/site.yml

printf "\n\nInstalling Shark Brokers..."
ansible-playbook /shark/Shark-Brokers/site.yml

printf "\n\nInstalling Shark Config..."
ansible-playbook /shark/Shark-Config/site.yml

printf "\n\nInstalling Shark Web..."
ansible-playbook /shark/Shark-Web/site.yml

printf "\n\nStarting httpd and nagios..."
systemctl restart httpd && systemctl restart nagios

printf "\n\nVerifying Shark config..."
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg

/usr/bin/figlet Finished.

printf "\nOpen a web browser and navigate to http://$(hostname --ip-address)/shark - (with shark/shark as username/password )\n"
