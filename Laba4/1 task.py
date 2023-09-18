n = int(input("Введите количество вершин: "))
matrix = [[0] * n for i in range(n)]
a, b = 0, 0
petli = False
smej = [x for x in range(1, n + 1)]

print("Введите граф. Для завершения вместо одного числа введите 0.")
while a != -1 and b != -1:
    a, b = map(int, input().split())
    if a in smej:
        smej.remove(a)
    if b in smej:
        smej.remove(b)

    a -= 1
    b -= 1
    if a != -1 and b != -1:
        if matrix[a][b] == 0:
            matrix[a][b] += 1
            matrix[b][a] += 1
        else:
            print("Этот путь уже введен.")
        if a == b:
            petli = True

print("a)")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print('\t', matrix[i][j], end=' ')
    print()

if petli:
    print('\t', "В графе есть петли.")
else:
    print('\t', "В графе нет петель.")

print("b)")
if len(smej) == 0:
    print('\t', "В графе все вершины смежные.")
else:
    print('\t', "Вершины, не смежные с другими: " + ' '.join(map(str, smej)))

print("в)")
for i in range(len(matrix)):
    print('\t', "Смежные вершины для вершины ", str(i + 1), ":",
          ' '.join(map(str, [x + 1 for x in range(len(matrix[i])) if matrix[i][x] != 0])))

print("г)")
flag = True
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0 and i != j:
            flag = False
    if flag:
        print('\t', "Вершина, смежная со всеми другим: ", i + 1)
    flag = True
if not (flag):
    print('\t', "Нет вершин, которые смежные со всеми другими.")

step1 = False
maxStep = 0
print("д)")
for i in range(len(matrix)):
    s = sum(matrix[i])
    if s == 1:
        step1 = True
    maxStep = max(maxStep, s)
    print('\t', "Степень вершины ", str(i + 1), " - ", str(s))

print("е)")
if step1:
    print('\t', "Вершины со степенью 1:", end=' ')
    for i in range(len(matrix)):
        if sum(matrix[i]) == 1:
            print(i + 1, end=' ')
    print()
else:
    print('\t', "Нет вершин со степенью 1.")

print("ж)")
print('\t', "Cтепень графа (максимальная степень его вершин) - ", maxStep)
