operator_name = input('Введите имя оператора: ')
pressure = float(input('Введите текущее значение давления (Па): '))

with open('sensor_log.txt', 'w', encoding='utf-8') as logs:
    logs.write('Оператор    | Давление\n')
    logs.write(f'{operator_name}    | {pressure}\n')

print('Данные успешно сохранены в sensor_log.txt')