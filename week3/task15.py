string = str(input())

first = string.find("f")

if first != -1:
    rev_str = string[::-1]
    sec = rev_str.find("f")
    if sec != -1:
        sec = len(string) - sec - 1
        if first != sec:
            print(first, sec, sep=" ")
        else:
            print(first)
