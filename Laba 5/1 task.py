import re

inputFile = open("resources/input.txt", encoding="utf-8")
outputFile = open("resources/output.txt", "w", encoding="utf-8")
cnt = 0
pattern = " .,!?/'\"{}[]()"

word = input("Введите слово: ")

cnt = sum([line.strip(pattern).lower().split().count(word) for line in inputFile])
outputFile.write("1.\tСлово '" + word + "' встречается в тексте " + str(cnt) + " раз.\n\n")

newWord = input("Введите новое слово: ")
outputFile.write("2. ")
inputFile.seek(0)
for line in inputFile:
    outputFile.write("\t" + line.replace(word, newWord))
outputFile.write("\n\n")

inputFile.seek(0)
cnt = 0
for line in inputFile:
    cnt += len([x for x in re.findall(r'\d+', line) if int(x) % 1 == 0])
outputFile.write("3. \tКоличество целых чисел в тексте: " + str(cnt) + "\n\n")

inputFile.seek(0)
outputFile.write("4. ")
for line in inputFile:
    outputFile.write("\t" + line.replace("  ", " "))
outputFile.write("\n\n")

word = input("Введите слово, которое нужно удалить: ")
inputFile.seek(0)
outputFile.write("5. ")
for line in inputFile:
    outputFile.write("\t" + line.replace(word, ''))
outputFile.write("\n\n")

inputFile.seek(0)
cnt = 0
for line in inputFile:
    for word in line.split():
        if word.strip(pattern)[0] == 'А':
            cnt += 1
outputFile.write("6.\tКоличество слов, начинающиеся буквой 'A': " + str(cnt) + "\n\n")

inputFile.seek(0)
cnt = 0
for line in inputFile:
    for word in line.split():
        if word.strip(pattern)[-1] == 'и':
            cnt += 1
outputFile.write("7.\tКоличество слов, начинающиеся буквой 'и': " + str(cnt) + "\n\n")

inputFile.seek(0)
cnt = 0
for line in inputFile:
    for word in line.split():
        if 'ло' in word:
            cnt += 1
outputFile.write("8.\tКоличество слов, содержащих слог 'ло': " + str(cnt) + "\n\n")

inputFile.seek(0)
cntOpen = 0
cntClose = 0
for line in inputFile:
    cntOpen += line.count('(')
    cntClose += line.count(')')
outputFile.write("9.\tКоличество открывающихся круглых скобок: " + str(cntOpen) + "\n")
outputFile.write("\tКоличество закрывающихся круглых скобок: " + str(cntClose) + "\n\n")

inputFile.seek(0)
outputFile.write("10. ")
for line in inputFile:
    if '{' in line and '}' in line:
        line = line.replace(line[line.index('{'):line.index('}') + 1], '')
    outputFile.write("\t" + line)
outputFile.write("\n\n")

maxCnt = 0
cnt = 1
lastChar = ''
inputFile.seek(0)
for line in inputFile:
    for c in line:
        if c == lastChar:
            cnt += 1
            maxCnt = max(maxCnt, cnt)
        else:
            cnt = 1
        lastChar = c
outputFile.write("11.\tНаибольшее число подрят идущих одинаковых символов: " + str(maxCnt) + "\n\n")

a = ord('а')
rusAlphabet = ''.join([chr(i) for i in range(a, a + 32)])
nums = "0123456789"
inputFile.seek(0)
cntChars = 0
cntNums = 0
for line in inputFile:
    for c in line:
        if c in rusAlphabet:
            cntChars += 1
        if c in nums:
            cntNums += 1
outputFile.write("12.\tКоличество букв: " + str(cntChars) + "\n")
outputFile.write("\tКоличество цифр: " + str(cntNums) + "\n")
message = "Цифр"
if cntChars>cntNums:
    message = "Букв"
outputFile.write("\t" + message + " больше.")

inputFile.close()
outputFile.close()
