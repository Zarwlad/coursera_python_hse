def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def ReduceFraction(n, m):
    c = gcd(n, m)
    return int(n / c), int(m / c)


a = int(input())
b = int(input())

print(*ReduceFraction(a, b))
