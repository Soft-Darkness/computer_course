culture_medium_name = input('Введите название питательной среды: ')
agar_concentration = float(input('Введите концентрацию агара (%): '))
sterilization_temperature = float(input('Введите температуру стерилизации (°C): '))

with open('recipe.txt', 'a', encoding='utf-8') as recipe:

    recipe.write(culture_medium_name.upper())
    recipe.write(f'\nКонцентрация агара: {agar_concentration}%\n')
    recipe.write(f'Температура стерилизации: {sterilization_temperature}°C\n\n')

print('Файл "Recipe.txt" успешно сформирован')