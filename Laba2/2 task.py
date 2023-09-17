string = ''
while len(string)<10:
    string = input("Введите фразу: ")
    if len(string)<10:
        print("Длина строки должна быть больше или равно 10.")

print("a) ", string[:4])
print("b) ", string[-4:])
l = len(string)
if l%2==0:
    print("c) ", string[l//2-1:l//2+1])
else:
    print("c) ", string[l//2])
print("d) ", string[2:8])