import time
import random
from threading import *

data = list()
path = "resources/output.txt"
with open(path, "w") as file:
    file.write("")

def addition(data):
    while True:
        data.append(random.randint(1, 100))
        time.sleep(1)


def display(data):
    while True:
        print(*data)
        time.sleep(1)


def sort(data, path):
    while True:
        with open(path, "a") as file:
            newData = data[:]
            newData.sort()
            file.write(str(" ".join(map(str, newData)) + '\n'))
        time.sleep(5)

addThr = Thread(target=addition, args=(data,))
disThr = Thread(target=display, args=(data, ))
sortThr = Thread(target=sort, args=(data, path))

addThr.start()
disThr.start()
time.sleep(5)
sortThr.start()

addThr.join()
disThr.join()
sortThr.join()
