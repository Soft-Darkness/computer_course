reagent_name = input('Введите название нового реактива: ')
reagent_count = int(input('Введите количество реактива: '))
file = open("inventory.txt", "a", encoding="utf-8")

print(f'Реактив {reagent_name} поступил на склад в количестве {reagent_count} шт.') # Вывод отчёта в консоль

print(f'Реактив {reagent_name} поступил на склад в количестве {reagent_count} шт.', file=file) # Запись отчёта в файл