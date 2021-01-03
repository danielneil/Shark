#/usr/bin/bash

ansible-playbook ./site.yml -i hosts

# Run the Nagios self sanity check.
 /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg