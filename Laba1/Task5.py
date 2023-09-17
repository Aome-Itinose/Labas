num = float(input("Введите число: "))

a = num % 10
num //= 10
b = num % 10
num //= 10
c = num % 10
num //= 10

s = a + b + c
pr = a * b * c

print("Сумма = ", s)
print("Произведение = ", pr)
