num = int(input())
i = 1

while True:
    root = i ** 2
    if root > num:
        break
    else:
        i = i + 1
        print(root, end=" ")
