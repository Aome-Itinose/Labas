num = float(input("Введите число: "))

a = num % 10
num //= 10
b = num % 10
num //= 10
c = num % 10
num //= 10

newNum = a * 100 + b * 10 + c
print("Число = ", newNum)
