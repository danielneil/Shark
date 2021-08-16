cd /tmp/nagios-4.4.6 &&                 
./configure &&                 
make all &&                 
make install-groups-users &&
usermod -a -G nagios apache &&
make install &&  
make install-daemoninit &&  
make install-commandmode &&                 
make install-config &&  
make install-webconf 
