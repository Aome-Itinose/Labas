n = 0
stops = []
matrix = []
with open("resources/InputForTwo.txt", 'r', encoding="utf-8") as file:
    n = int(file.readline())
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        stops.append(file.readline().strip())
    for i in range(n):
        line = list(map(int, file.readline().split()))
        for j in range(n):
            matrix[i][j] = line[j]
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
while min_dist < INF:
    i = min_vertex
    used[i] = True
    for j in range(n):
        if matrix[i][j] != 0:
            dist[j] = min(dist[j], dist[i] + matrix[i][j])
    min_dist = INF
    for j in range(n):
        if not (used[j]) and dist[j] < min_dist:
            min_dist = dist[j]
            min_vertex = j
print("Длина кратчайшего пути: ", dist[end])
