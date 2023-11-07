import re

inputFile = open("resources/input.txt", encoding="utf-8")
outputFile = open("resources/output.txt", "w", encoding="utf-8")
cnt = 0
pattern = " .,!?/'\"{}[]()"


def countWord(word):
    return sum([line.strip(pattern).lower().split().count(word) for line in inputFile])


def replaceAllWords(word, newWord):
    inputFile.seek(0)

    for line in inputFile:
        outputFile.write("\t" + line.replace(word, newWord))
    outputFile.write("\n\n")


def integersInText():
    inputFile.seek(0)
    cnt = 0
    for line in inputFile:
        cnt += len([x for x in re.findall(r'\d+', line) if int(x) % 1 == 0])
    return cnt


def removeExtraSpaces():
    inputFile.seek(0)
    for line in inputFile:
        outputFile.write("\t" + line.replace("  ", " "))


def removeWordInText(word):
    inputFile.seek(0)
    for line in inputFile:
        outputFile.write("\t" + line.replace(word, ''))


def countWordsStartsAt(char):
    inputFile.seek(0)
    cnt = 0
    for line in inputFile:
        for word in line.split():
            if word.strip(pattern)[0] == char:
                cnt += 1
    return cnt


def countWordsFinishAt(char):
    inputFile.seek(0)
    cnt = 0
    for line in inputFile:
        for word in line.split():
            if word.strip(pattern)[-1] == char:
                cnt += 1
    return cnt


def countWordsWith(char):
    inputFile.seek(0)
    cnt = 0
    for line in inputFile:
        for word in line.split():
            if char in word:
                cnt += 1
    return cnt


def countScopes():
    inputFile.seek(0)
    cntOpen = 0
    cntClose = 0
    for line in inputFile:
        cntOpen += line.count('(')
        cntClose += line.count(')')
    return [cntOpen, cntClose]


def deleteScopes():
    inputFile.seek(0)
    for line in inputFile:
        if '{' in line and '}' in line:
            line = line.replace(line[line.index('{'):line.index('}') + 1], '')
        outputFile.write("\t" + line)


def largestNumberOfConsecutiveIdenticalCharacters():
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
    return maxCnt

def countCharNumber():
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
    return [cntChars, cntNums]


word = input("Введите слово: ")

outputFile.write("1.\tСлово '" + str(word) + "' встречается в тексте " + str(countWord(word)) + " раз.\n\n")

newWord = input("Введите новое слово: ")
outputFile.write("2. ")
replaceAllWords(word, newWord)

integersInText()
outputFile.write("3. \tКоличество целых чисел в тексте: " + str(integersInText()) + "\n\n")

outputFile.write("4. ")
removeExtraSpaces()
outputFile.write("\n\n")

word = input("Введите слово, которое нужно удалить: ")
outputFile.write("5. ")
removeWordInText(word)
outputFile.write("\n\n")

outputFile.write("6.\tКоличество слов, начинающиеся буквой 'A': " + str(countWordsStartsAt('А')) + "\n\n")

outputFile.write("7.\tКоличество слов, заканчивающиеся буквой 'и': " + str(countWordsFinishAt('и')) + "\n\n")

outputFile.write("8.\tКоличество слов, содержащих слог 'ло': " + str(countWordsWith('ло')) + "\n\n")

outputFile.write("9.\tКоличество открывающихся круглых скобок: " + str(countScopes()[0]) + "\n")
outputFile.write("\tКоличество закрывающихся круглых скобок: " + str(countScopes()[1]) + "\n\n")

outputFile.write("10. ")
deleteScopes()
outputFile.write("\n\n")

outputFile.write("11.\tНаибольшее число подрят идущих одинаковых символов: "
                 + str(largestNumberOfConsecutiveIdenticalCharacters()) + "\n\n")

cntChars, cntNums = countCharNumber()
outputFile.write("12.\tКоличество букв: " + str(cntChars) + "\n")
outputFile.write("\tКоличество цифр: " + str(cntNums) + "\n")
message = "Цифр"
if cntChars > cntNums:
    message = "Букв"
outputFile.write("\t" + message + " больше.")

inputFile.close()
outputFile.close()
