import pandas as pd

n = 0
stops = []
with open("resources/InputForTwo.txt", 'r', encoding="utf-8") as file:
    n = int(file.readline())
    for i in range(n):
        stops.append(file.readline().strip())

matrix = pd.read_excel("inM.xlsx")

for i in range(n):
    print(str(i), '-', stops[i])


start = int(input("Введите начальную точку: ")) - 1
end = int(input("Введите конечную точку: ")) - 1

INF = 10 ** 10
used = [False] * n
min_dist = 0
min_vertex = start
dist = [INF] * n
dist[start] = 0
paths = [[start + 1]] * n
while min_dist < INF:
    i = min_vertex
    used[i] = True
    for j in range(n):
        if matrix[i][j] != 0:
            if dist[j] > dist[i] + matrix[i][j]:
                dist[j] = dist[i] + matrix[i][j]
                paths[j] = paths[i] + [j + 1]
    min_dist = INF
    for j in range(n):
        if not (used[j]) and dist[j] < min_dist:
            min_dist = dist[j]
            min_vertex = j
            minPath = paths[j]

print("Длина кратчайшего пути: ", dist[end])
minPath = paths[end][::-1]
for i in range(len(minPath) - 1):
    print(stops[minPath[i] - 1], end=" <- ")
print(stops[minPath[-1] - 1])
