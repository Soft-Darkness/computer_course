#!/bin/bash

echo "Названия товаров:"
awk -F "," '{print $2}' $1
echo "Дороже 20 стоят:"
awk -F "," '{
	if ($3 > 20)
		 print $2
}' $1
awk -F "," '{sum += $3} END{print "Общая стоимоть: ", sum}' $1
