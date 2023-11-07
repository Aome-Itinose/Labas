n = int(input("Введите число n: "))
data = [x for x in range(2, n + 1)]
krat7 = [x for x in range(2, n + 1) if x % 7 == 0]

i = 0
pop = int(n ** 0.5)
while i < len(data):
    if data[i] > pop:
        break
    j = i + 1
    while j<len(data):
        if data[j]%data[i]==0:
            del(data[j])
            j -= 1
        j += 1
    i += 1
print(*data)
print(*krat7)
