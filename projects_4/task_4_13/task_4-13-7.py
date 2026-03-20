n = int(input("Сколько элементов будет в массиве? "))
array = []
sum = 0

for i in range(n):
    element = int(input(f"Введите значение элемента(число): "))
    array.append(element)

j = 0
for j in range(n):
    sum = sum + array[j]

mid = sum / n
print(mid)