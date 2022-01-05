#/usr/bin/bash

##################################################
# Exit when any command fails
set -e

##################################################
# Installing Shark.
ansible-playbook ./site.yml -i hosts --ssh-extra-args='-o ServerAliveInterval=3600'

# Installing the Shark Plugins.
ansible-playbook /var/www/shark-git/Shark-Plugins/site.yml -i hosts

# Verifying Nagios config.
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg

# Startin httpd and nagios.
systemctl start httpd && systemctl start nagios
