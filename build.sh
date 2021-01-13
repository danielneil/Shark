#/usr/bin/bash

# Generate the documentation for the plugins
CURR_DIR=`pwd`
CHECKS_PATH=automatedtradingplatform/files/nagios_plugins
DOC_FILE=README.PLUGINS.md

echo "# Plugins Documentation" > ${DOC_FILE}

echo "" >> ${DOC_FILE}
echo "This is the plugins documentation." >> ${DOC_FILE}
echo "Plugins are structured the same as traditional nagios plugins." >> ${DOC_FILE}
echo "" >> ${DOC_FILE}

for CHECK_cmd in `find $CHECKS_PATH | grep check_`
do
	echo "## $(basename $CHECK_cmd | sed 's/.py//g')" >> ${DOC_FILE}
	echo "" >> ${DOC_FILE}

	printf "`$CHECK_cmd --help`" >> ${DOC_FILE}
	echo "" >> ${DOC_FILE}
done

echo "" >> ${DOC_FILE}
echo "" >> ${DOC_FILE}
echo "This documentation is automatically generated, do not edit this file, instead amend the help text in the plugin's source code." >> ${DOC_FILE}

# Make some pretties

sed 's/usage:/**Usage:**/g' -i ${DOC_FILE}
sed 's/optional arguments/**Optional Arguments**/g' -i ${DOC_FILE}

cd $CURR_DIR;

# Now run the playbook.
ansible-playbook ./site.yml -i hosts