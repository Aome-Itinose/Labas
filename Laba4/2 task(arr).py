n = int(input("Введите число n: "))
if n == 1:
    print(1)
else:
    data = [1] * (n + 1)
    for i in range(2, n + 1):
        data[i] = i - data[data[i - 1]]
    print(data[n])

