def polind(n, x):
    if n == 0:
        return 1
    if n == 1:
        return x
    return ((2 * n - 1) * polind(n - 1, x) - (n - 1) * polind(n - 2, x)) / n
print(polind(int(input("Введите порядок n: ")), int(input("Введите число x: "))))
