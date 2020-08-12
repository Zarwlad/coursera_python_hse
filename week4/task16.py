def inp(a):
    b = int(input())

    if b != 0:
        a += b
        inp(a)
    else:
        print(a)
        return a


inp(0)
