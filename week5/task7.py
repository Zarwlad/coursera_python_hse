a = int(input())

i = 1
while i <= a:
    c = tuple(range(1, i + 1))

    for b in c:
        print(b, end="")
    print()
    i += 1
