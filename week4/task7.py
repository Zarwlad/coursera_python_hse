import math


def IsPointInCircle(x, y, xc, yc, r):
    h = math.sqrt((x - xc) ** 2 + (y - yc) ** 2)
    return h <= r


x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())

if IsPointInCircle(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")
