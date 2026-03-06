#!/bin/bash

echo -n "Сумма оценок: "; awk '{ sum += $2 } END{ print sum } ' $1
awk '{ mid += $2 }{ i++ } END{print "Средняя оценка: ", mid / i}' $1
awk 'NR==1{ max = $2 } $2 > max{ max=$2 } END{ print "Максимальная оценка: ", max }' $1
