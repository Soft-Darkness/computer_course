weight = float(input('Введите ваш вес(кг): '))
height = float(input('Введите ваш рост(м): '))

bmi = weight / (height ** 2)

print('--- Отчёт о состоянии здоровья ---')
print(f'Вес: \t{weight}кг')
print(f'Рост: \t{height*100} см')
print(f'Индекс массы тела: \t {weight / (height ** 2):.2f}')