phenotype_funder = input("Введите фенотип группы крови донора(I, II, III, IV): ").strip().upper()
phenotype_recepient = input('Введите фенотип группы крови реципиента: ').strip().upper()

if phenotype_funder != "I" and phenotype_funder != "II" and phenotype_funder != "III" and phenotype_funder != "IV":
    print('Такой группы крови не существует')
elif phenotype_funder == "I":
    print('Можете переливать кровь реципиенту')
elif phenotype_funder == "II" and (phenotype_recepient == "II" or phenotype_recepient == "IV"):
    print('Можете переливать кровь реципиенту')
elif phenotype_funder == "III" and (phenotype_recepient == "III" or phenotype_recepient == "IV"):
    print('Можете переливать кровь реципиенту')
elif phenotype_funder == "IV" and phenotype_recepient == "IV":
    print('Можете переливать кровь')
else:
    print('Кровь переливать нельзя')