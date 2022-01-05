#/usr/bin/bash

##################################################
# Exit when any command fails
set -e

##################################################
# Run the playbook.
ansible-playbook ./site.yml -i hosts --ssh-extra-args='-o ServerAliveInterval=3600'

# Installing the plugins.
ansible-playbook /var/www/shark-git/Shark-Plugins/site.yml -i hosts
