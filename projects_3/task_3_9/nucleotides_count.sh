#!/bin/bash

printf  "%-20s %-10s %-10s %-10s  %-10s\n" "File" "A" "T" "G" "C"

for file in *.fasta; do
	if [ ! -s "$file" ]; then continue; fi

seq=$(grep -v "^>" "$file" | tr -d '\n')
a=$(echo "$seq" | grep -o "A" | wc -l)
g=$(echo "$seq" | grep -o "G" | wc -l)
c=$(echo "$seq" | grep -o "C" | wc -l)
t=$(echo "$seq" | grep -o "T" | wc -l)

printf "%-20.20s %-10s %-10s %-10s %-10s\n" "$file" "$a" "$t" "$g" "$c"
done
echo -e "\e]8;;ftp.ensembl.org/pub/release-86/fasta/caenorhabditis_elegans/dna/\e\\Для проверки кода использовались файлы:\e]8;;\e\\"
