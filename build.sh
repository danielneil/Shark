#/usr/bin/bash

if ! `which figlet > /dev/null` ; then
  dnf install figlet -y > /dev/null
fi
/usr/bin/figlet Shark

# Installing Shark.
ansible-playbook ./site.yml -i hosts --ssh-extra-args='-o ServerAliveInterval=3600'

# Installing the Shark Plugins.
ansible-playbook /shark/Shark-Plugins/site.yml -i hosts

# Startin httpd and nagios.
systemctl restart httpd && systemctl restart nagios

# Verifying Nagios config.
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
