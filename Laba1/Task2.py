from math import pi

r1 = float(input("Введите радиус первого круга: "))
r2 = float(input("Введите радиус второго круга: "))
s1 = r1 ** 2 * pi
s2 = r2 ** 2 * pi
s3 = s1 - s2
print("Площадь первого круга равна: ", s1)
print("Площадь второго круга равна: ", s2)
print("Площадь колца равна: ", s3)