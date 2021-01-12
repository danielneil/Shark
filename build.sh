#/usr/bin/bash


# Generate the documentation for the plugins
CURR_DIR=`pwd`
CHECKS_PATH=automatedtradingplatform/files/nagios_plugins
DOC_FILE=PLUGINS.HELP

echo "# Documentation for Plugins" > ${DOC_FILE}

for CHECK_cmd in `find $CHECKS_PATH | grep check_`
do
	echo "## $CHECK_cmd" >> ${DOC_FILE}
	echo "" >> ${DOC_FILE}

	echo "`$CHECK_cmd --help`" >> ${DOC_FILE}
	echo "" >> ${DOC_FILE}
done

cd $CURR_DIR;

# Now run the playbook.
ansible-playbook ./site.yml -i hosts
