#!/usr/bin/bash

echo "Verifying YAML"

if [ ! `which yamllint` ]; then
  echo "Install yamllint please, exiting..."
  exit 1
fi

XMLLINT=`which yamllint`

$XMLLINT trading-config.yml

if [ $? -ne 0  ]; then
 echo "Invalid YAML, exiting..."
 exit 1
fi

echo "YAML config looks fine...."
exit 0
