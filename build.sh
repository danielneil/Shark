#/usr/bin/bash

# exit when any command fails
set -e

##################################################
# Generate the documentation for the plugins

CURR_DIR=`pwd`
CHECKS_PATH=shark/files/plugins
DOC_FILE=doc/README.PLUGINS.md

generate_documentation() {

	echo "# Plugins Documentation" > ${DOC_FILE}

	echo "" >> ${DOC_FILE}
	echo "This is the plugins documentation." >> ${DOC_FILE}
	echo "" >> ${DOC_FILE}
	echo "The plugins enable the platform to monitor and alert on just about **anything** of interest; if its online, it can be monitored." >> ${DOC_FILE}
	echo "" >> ${DOC_FILE}

	# Generate the table of contents.

	echo "# Contents" >> ${DOC_FILE}

	for CHECK_cmd in `find $CHECKS_PATH | grep check_`
	do
    		plugin_name=$(basename $CHECK_cmd | sed 's/.py//g')

		# If this is the check_template, skip.
		if [ $plugin_name == "check_template" ];
		then
			continue;
		fi

		echo "* [$plugin_name](#$plugin_name)" >> ${DOC_FILE}
	done

	# Generate the body.

	for CHECK_cmd in `find $CHECKS_PATH | grep check_`
	do
    		plugin_name=$(basename $CHECK_cmd | sed 's/.py//g')

		# If this is the check_template, skip.
		if [ $plugin_name == "check_template" ];
		then
			continue;
		fi

		echo "## <a name=\"$plugin_name\"/>$plugin_name" >> ${DOC_FILE}
		echo "" >> ${DOC_FILE}

		printf "`$CHECK_cmd --help`" >> ${DOC_FILE}
		echo "" >> ${DOC_FILE}
	done

	echo "" >> ${DOC_FILE}
	echo "" >> ${DOC_FILE}
	echo "This is automatically generated, do not edit this file, instead amend the help text in the plugin's source code." >> ${DOC_FILE}

	# Make some pretties

	sed 's/usage:/**Usage:**/g' -i ${DOC_FILE}
	sed 's/optional arguments/**Optional Arguments**/g' -i ${DOC_FILE}

	cd $CURR_DIR;

}

##################################################
# Now run the playbook.
ansible-playbook ./site.yml -i hosts --ssh-extra-args='-o ServerAliveInterval=3600'

##################################################
# Generate the configuration
generate_documentation

##################################################
# Verify the nagios configuration - this is purely used for debugging. 
ansible shark -i hosts -a 'sudo /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg'
