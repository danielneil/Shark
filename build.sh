#!/usr/bin/bash -x

if ! `which figlet 2> /dev/null` ; then
  dnf install figlet -y > /dev/null
fi

echo "SDF"

if ! `which jp2a 2> /dev/null` ; then
 dnf install -y https://tchung.org/jp2a/files/jp2a-1.0.8-1.el8.x86_64.rpm > /dev/null
fi

/usr/bin/figlet Shark
printf "The Algorithmic Trading Platform..."
printf "\nAuthor: danielneil"
jp2a shark/files/screenshots/shark.jpg --background=light

printf "\n\nInstalling Shark..."
ansible-playbook ./site.yml -i hosts --ssh-extra-args='-o ServerAliveInterval=3600'

printf "\n\nInstalling the Shark Plugins..."
ansible-playbook /shark/Shark-Plugins/site.yml -i hosts

printf "\n\nStarting httpd and nagios..."
systemctl restart httpd && systemctl restart nagios

printf "\n\nVerifying Shark config..."
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg

/usr/bin/figlet Finished.
