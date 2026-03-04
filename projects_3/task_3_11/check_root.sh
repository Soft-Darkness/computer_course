#!/bin/bash

check_root () {
	if [ "$EUID" -ne 0 ]; then
		echo "Ошибка запуска! Запустите скрипт от имени администратора"
		exit 1
	fi
}

check_root

echo 'Скрипт запущен суперпользователем'
