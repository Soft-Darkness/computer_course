n = int(input("Сколько элементов будет в массиве? "))
array = []
sum = 0
count = 0

for i in range(n):
    element = int(input(f"Введите значение элемента(число): "))
    array.append(element)

for j in range(n):
    if j % 2 == 0:
        sum += array[j]
        count += 1

print(sum / count)