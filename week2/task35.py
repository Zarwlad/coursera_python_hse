inputs = int(input())
even = 0

while inputs != 0:
    if inputs % 2 == 0:
        even = even + 1
    inputs = int(input())
print(even)
