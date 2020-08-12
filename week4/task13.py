def degree(a, b):
    if b % 2 == 0:
        b = b / 2
        return (a * a) ** b
    else:
        return a * a ** (b - 1)


a = float(input())
b = int(input())
print(degree(a, b))
