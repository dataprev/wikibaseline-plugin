#!/bin/sh

# just for first development deploy

if [ ! $1 ]; then
  echo "usage: $0 path-to-deploy-it"
  exit 1
fi

# sanity checker
if [ ! -d $1  ]; then
  echo "Sanity checker..."
  echo $1 "are not a valid dirname. Please check if directory exist and you have access to it"
  exit 1
fi

if [ -f $1/../VERSION ]; then
	python setup.py develop -mxd $1
else
	echo "$1 does not seem a valid TracEnv"
   exit 1
fi 

