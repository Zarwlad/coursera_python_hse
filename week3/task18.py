string = str(input())

first = string.find("f")

if first != -1:
    sec = string.find("f", first + 1)
    if sec != -1:
        print(sec)
    else:
        print(-1)
else:
    print(-2)
