n = int(input())
max = 0
for i in range(1, n+1):
    a = float(input())
    if a > max:
        max = a

print(max)