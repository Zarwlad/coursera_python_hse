def inp():
    b = int(input())

    if b != 0:
        inp()
    print(b)


inp()
