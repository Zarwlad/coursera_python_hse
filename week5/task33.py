s = list(map(int, input().split()))

x_min = 3_000_000_000
x_max = -3_000_000_000
x_min_i = 0
x_max_i = 0

for n in s:
    if x_min > n:
        x_min = n
        x_min_i = s.index(n)
    if x_max < n:
        x_max = n
        x_max_i = s.index(n)

s.__setitem__(x_max_i, x_min)
s.__setitem__(x_min_i, x_max)

print(*s)
