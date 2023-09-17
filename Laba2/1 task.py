x = float(input("Введите число x: "))
n = -1
while n<0:
    n = int(input("Введите число n: "))
    if n<0:
        print("Число n должно быть больше или равно 0.")

s = 0
xx = 1
fact_n = 1
flag = True
for i in range(n + 1):
    if flag:
        s += xx / fact_n
        xx *= (x * x)
        fact_n *= (i+1)
        flag = not (flag)
    else:
        s -= xx / fact_n
        xx *= (x * x)
        fact_n *= (i+1)
        flag = not (flag)
print(s)
