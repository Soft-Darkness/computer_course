fio = input('Введите своё ФИО: ')
date = input('Введите дату проведения эксперимента: ')
experiment_name = input('Введите название эксперимента: ')
experiment_number = (input('Введите номер эксперимента: '))
experiment_conclusion = input('Введите вывод: ')
border = '+' + '-'*60 + '+\n' # граница
width = 58 # ширина таблицы

with open('journal.txt', 'a', encoding='utf-8') as journal:
    journal.write(border)

    journal.write(f'| {f"Эксперимент №{experiment_number}":<{width}} |\n')
    journal.write(border)
    journal.write(f'| {f"ФИО исследователя : {fio}":<{width}} |\n')
    journal.write(f'| {f"Дата : {date}":<{width}} |\n')
    journal.write(f'| {f"Эксперимент : {experiment_name}":<{width}} |\n')
    journal.write(border)
    journal.write(f'| {"Вывод:":<{width}} |\n')
    for i in range(0, len(experiment_conclusion) or 1, width):
        journal.write(f'| {experiment_conclusion[i:i+width]:<{width}} |\n')

    journal.write(border)