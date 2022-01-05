#/usr/bin/bash

if ! `which figlet > /dev/null` ; then
  dnf install figlet -y > /dev/null
fi

if ! `which jp2a > /dev/null` ; then
 dnf -y install https://tchung.org/jp2a/files/jp2a-1.0.8-1.el8.x86_64.rpm
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
