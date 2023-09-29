inputFile = open("resources/input.txt", encoding="utf-8")
outputFile = open("resources/output.txt", "w", encoding="utf-8")
cnt = 0
word = input("Введите слово: ")
for line in inputFile:
    line = line.strip(",.!? ").lower().split()
    cnt += line.count(word)

outputFile.write("Слово '" + word + "' встречается в тексте " + str(cnt) + " раз.")
