data = list()
while len(data)!=6:
        data = list(map(int, input("Введите шесть цифр через запятую: ").split(',')))
print("a) ",data[3])
print("b) ", *data[5::-1])
s = sum(data)
sred_arifm = s/6
print("c) Сумма = ",s, ", средняя арифметическая = ", sred_arifm,"." )
