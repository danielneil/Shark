#/usr/bin/bash

if ! `which figlet > /dev/null` ; then
  dnf install figlet -y > /dev/null
fi
/usr/bin/figlet Shark
printf "The Algorithmic Trading Platform..."

printf "\nInstalling Shark..."
ansible-playbook ./site.yml -i hosts --ssh-extra-args='-o ServerAliveInterval=3600'

printf "\nInstalling the Shark Plugins..."
ansible-playbook /shark/Shark-Plugins/site.yml -i hosts

printf "\nStarting httpd and nagios..."
systemctl restart httpd && systemctl restart nagios

printf "\nVerifying Shark config..."
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
