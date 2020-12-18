cd /tmp/nagios-4.4.6 &&                 
./configure --with-httpd-conf=/etc/apache2/sites-enabled &&                 
make all &&                 
make install-groups-users &&                 
usermod -a -G nagios www-data && 
make install &&  
make install-daemoninit &&  
make install-commandmode &&                 
make install-config &&  
make install-webconf &&  
a2enmod rewrite &&  
a2enmod cgi
