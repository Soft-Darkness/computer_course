capsules_count = int(input('Введите количество произведённых капсул: '))
pack_capacity = int(input('Введите вместимость одной упаковки: '))

print('---Отчёт фасовочного цеха---')
print(f'Полных упаковок: {capsules_count // pack_capacity}')
print(f'Остаток капсул: {capsules_count % pack_capacity}')