protein_mass = float(input('Введите массу белков:(г) '))
fats_mass = float(input('Введите массу жиров(г): '))
carbohydrates_mass = float(input('Введите массу углеводов(г): '))

print('Общая каллорийность: ', protein_mass*4 + fats_mass*9 + carbohydrates_mass*4)