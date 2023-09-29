n = int(input("Введите количество вершин: "))
print("Чтобы закончить введите 0.")
a, b = 1, 1
data = list()
while a != -1 and b != -1:
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a == -1 or b == -1:
        break
    data.append([a, b])

l = len(data)
matrix = [[0] * l for i in range(n)]
for i in range(len(data)):
    matrix[data[i][0]][i] += 1
    matrix[data[i][1]][i] += 1

for i in matrix:
    print("\t", *i)

print("a) ")
for i in range(len(matrix)):
    print("\tИнцедентные ребра для вершины ", i + 1, " :",
          ' '.join([str(j + 1) for j in range(len(matrix[i])) if matrix[i][j] != 0]))

print("б) ")
for i in range(len(matrix)):
    print("\tСтепень вершины ", i + 1, " :", sum(matrix[i]))

print("в) ")
step0 = list()
for i in range(len(matrix)):
    if sum(matrix[i]) == 0:
        step0.append(i + 1)
if len(step0) == 0:
    print("\tНет вершин со степенью 0.")
else:
    print("\tВершины со степенью 0:", ' '.join(map(str, step0)))

print("г) ")
step1 = list()
for i in range(len(matrix)):
    s = sum(matrix[i])
    if s == 1:
        step1.append(s)
if len(step1) == 0:
    print("\tНет вершин, инцедентных только одному ребру.")
else:
    print("\tКоличество вершин, инцедентных только одному ребру: ", len(step1))

print("д) ")
print("\tНаибольшее число смежных между собой ребер, инцидентных одной и той же вершине: ",
      max([sum([1 for j in range(len(matrix[i])) if matrix[i][j] > 0]) for i in range(len(matrix))]))

print("е) ")
print("\tКоличество петель в графе: ", sum([1 for i in range(len(matrix)) if 2 in matrix[i]]))