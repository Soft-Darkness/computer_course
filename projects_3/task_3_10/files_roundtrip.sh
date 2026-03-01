#!/bin/bash

for i in {1..10}; do
	touch  "test$i.txt"
	echo "Создан файл: test$i.txt"
done

echo "---Files created---"

i=10
while [ "$i" -ge 1 ]; do
	file="test$i.txt"

	if [ -f "$file" ]; then
		rm -v "$file"
	fi
	((i--))
done

echo "---Files deleted---"
