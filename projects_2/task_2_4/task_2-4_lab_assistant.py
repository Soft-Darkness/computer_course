volume = float(input('Введите объём раствора(мл): '))
NaCl_mass = round(volume * 0.009, 2)
with open('recipe.txt', 'w', encoding='utf-8') as recipe:
    recipe.write('ОТЧЁТ ПО ПРИГОТОВЛЕНИЮ\n')
    recipe.write('-' * 23)
    recipe.write(f'\nОбщий объём: {volume} мл\nМасса соли: {NaCl_mass} г\nОбъём воды: {volume} мл')