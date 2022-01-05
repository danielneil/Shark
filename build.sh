#/usr/bin/bash

if ! `which figlet > /dev/null` ; then
  dnf install figlet -y > /dev/null
fi
/usr/bin/figlet Shark
echo "The Algorithmic Trading Platform..."

echo "\nInstalling Shark..."
ansible-playbook ./site.yml -i hosts --ssh-extra-args='-o ServerAliveInterval=3600'

echo "\nInstalling the Shark Plugins..."
ansible-playbook /shark/Shark-Plugins/site.yml -i hosts

echo "\nStarting httpd and nagios..."
systemctl restart httpd && systemctl restart nagios

echo "\nVerifying Shark config..."
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
