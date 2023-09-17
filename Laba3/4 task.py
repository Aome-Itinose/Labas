n = int(input("Введите число n: "))
data = [x for x in range(2, n + 1)]
krat7 = [x for x in range(2,n+1) if x%7==0]
p, i = 0, 0
while i < len(data):
    p = data[i]
    j = 0
    while j < len(data):
        if j != i and data[j] % p == 0:
            del[data[j]]
            if i>j:
                i-=1
            j-=1
        j+=1
    i+=1
print("a) Числа, кратные 7: ",*krat7)
print("b) Простые числа: ", *data)