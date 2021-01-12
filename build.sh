#/usr/bin/bash


# Generate the documentation for the plugins
CURR_DIR=`pwd`
CHECKS_PATH=automatedtradingplatform/files/nagios_plugins
DOC_FILE=PLUGINS.HELP.md

echo "# Documentation for Plugins" > ${DOC_FILE}

for CHECK_cmd in `find $CHECKS_PATH | grep check_`
do
	echo "## $(basename $CHECK_cmd)" >> ${DOC_FILE}
	echo "" >> ${DOC_FILE}

	printf "`$CHECK_cmd --help`" >> ${DOC_FILE}
	echo "" >> ${DOC_FILE}
done

echo "" >> ${DOC_FILE}
echo "This documentation is automatically generated." >> ${DOC_FILE}

# Make some pretties

sed 's/usage:/**Usage:**/g' -i ${DOC_FILE}
sed 's/optional arguments/**Optional Arguments**/g' -i ${DOC_FILE}
sed 's/\r/  /g' -i ${DOC_FILE}

cd $CURR_DIR;

exit 0;

# Now run the playbook.
ansible-playbook ./site.yml -i hosts
