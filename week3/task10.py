import math
# ax²+bx+c=0

a, b, c = float(input()), float(input()), float(input())

# дискриминант
d = b**2 - 4 * a * c

if d > 0:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    if x1 % 1 == 0:
        x1 = int(x1)
    if x2 % 1 == 0:
        x2 = int(x2)

    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)

elif d == 0:
    x = -b / (2 * a)
    if x % 1 == 0:
        x = int(x)
    print(x)
