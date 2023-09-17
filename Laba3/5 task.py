import random

n = int(input("Введите порядок матрицы: "))
data = list()
for i in range(n):
    data.append(list())
    for j in range(n):
        data[i].append(random.randint(0, 2))

cnt = 0
for i in range(n):
    if data[i][i] == 0:
        cnt += 1
    if data[i][n - i - 1] == 0:
        cnt += 1

if n%2==1 and data[n//2][n//2]==0:
    cnt -= 1
print(cnt)