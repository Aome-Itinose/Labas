with open("resources/input.txt", encoding="utf-8") as file:
    cnt = 0
    word = input("Введите слово: ")
    for line in file:
        line = line.strip(",.!? ").lower().split()
        cnt += line.count(word)

    print(cnt)

