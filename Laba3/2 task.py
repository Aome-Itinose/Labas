import random

data = list()
n = int(input("Введите количество элементов в массиве: "))
for i in range(n):
    data.append(random.randint(-1000, 1000))

firstData = list()
secondData = list()
for i in range(0, n):
    if data[i] < 0 and i % 2 == 1:
        firstData.append(data[i])
    else:
        secondData.append(data[i])

print(*(firstData + secondData))
