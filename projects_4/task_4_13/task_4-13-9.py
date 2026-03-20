n = int(input("Сколько элементов будет в массиве? "))
array = []
sum = 0

for i in range(n):
    element = int(input(f"Введите значение элемента(число): "))
    array.append(element)

for j in range(n):
    if array[j] % 2 != 0:
        sum = sum + array[j]

print(sum)