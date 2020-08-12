a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

if d >= a and (e >= b or e >= c):
    print("YES")
elif d >= b and (e >= a or e >= c):
    print("YES")
elif d >= c and (e >= a or e >= b):
    print("YES")
else:
    print("NO")
