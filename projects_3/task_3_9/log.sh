#!/bin/bash

file_path="./system.log"
error_code=1

if [ -f "$file_path" ]; then
	echo "Лог-файл найден."
else
	echo "Ошибка: файл не существует."
fi

case $error_code in
	0)
		echo "Статус: Ошибок нет." ;;
	1)
		echo "Статус: Критическая ошибка!" ;;
	*)
		echo "Неизвестный код." ;;
esac
