#!/bin/bash

awk '{print $1}
{print $2}
{print NR".", $1 "\n"}
' $1
