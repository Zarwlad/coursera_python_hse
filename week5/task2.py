a = int(input())
b = int(input())

c = 0
if a < b:
    c = range(a, b + 1)
else:
    c = range(a, b - 1, -1)

for i in c:
    print(i, end=" ")
