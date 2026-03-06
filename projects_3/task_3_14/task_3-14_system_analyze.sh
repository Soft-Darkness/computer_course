#!/bin/bash

df -h | awk 'NR == 1  {next} {print $1, $5} {
	if (int($5) > 90){
		print "WARNING: not enough space"
	}
}'
