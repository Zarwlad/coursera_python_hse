import math


def MinDivisor(n):
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    divisor = 5
    increment = 2
    sqrt_n = math.ceil(math.sqrt(n))
    while divisor <= sqrt_n:
        if n % divisor == 0:
            return divisor
        divisor += increment
        increment = 6 - increment

    return n


n = int(input())
print(MinDivisor(n))
