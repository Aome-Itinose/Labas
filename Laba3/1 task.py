string = ''
while len(string)==0 or string[-1]!='.':
    string = input("Введите строку заканчивающуюся точкой: ").strip()

print("a) Длина строки с точкой ", len(string))
data = string.strip().split()
print("b) Количество слов равна ", len(data))
print("c) Длина самого короткого слова: ", min(map(len, data)))
print("d) Преобразованная строки: ", "".join(x*2 for x in string.replace("*", "")))
