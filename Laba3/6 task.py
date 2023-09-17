import random

data = list()
for x in range(3):
    data.append(list())
    for y in range(5):
        data[x].append(list())
        for z in range(7):
            data[x][y].append(random.randint(-1000, 1000))

maxVal = -1001
resX, resY, resZ = 0, 0, 0
for x in range(len(data)):
    for y in range(len(data[x])):
        for z in range(len(data[x][y])):
            if maxVal < data[x][y][z]:
                maxVal = data[x][y][z]
                resX = x
                resY = y
                resZ = z
print("Максимальное значение: ", maxVal, ",x = ", resX, "y = ", resY, "z = ", resZ)
