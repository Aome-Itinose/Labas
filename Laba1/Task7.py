num = float(input("Введите число: "))

c = num // 100
newNum = (num % 100) * 10 + c

print("Число = ", newNum)