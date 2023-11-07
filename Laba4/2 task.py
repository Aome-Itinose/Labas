import sys

sys.setrecursionlimit(2000)
def p(n):
    if n == 1:
        return 1
    return n - p(p(n - 1))

print(p(int(input("Число: "))))