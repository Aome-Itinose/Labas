import random

n = int(input("Введите количество элементов в массиве: "))
data = list()
for i in range(n):
    data.append(random.randint(-1000, 1000))

print(*data)

start, finish = -1, -1
flag = False
i = 0
while i < len(data):
    if data[i] > 0:
        if flag == False:
            start = i
            flag = True
        elif i - start > 2:
            finish = i
            del data[start+1:finish]
            i = finish-1
            flag = False
        else:
            start = i
    i+=1
print(*data)
