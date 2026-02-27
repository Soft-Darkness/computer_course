#!/bin/bash

read -p "Введите вашу массу (кг): " mass
read -p "Введите ваш рост (см): " height
BMI=$((mass * 10000  / (height * height)))
echo "Ваш ИМТ = ${BMI%.*}" 
