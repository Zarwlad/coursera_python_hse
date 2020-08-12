a = list(map(int, input().split()))
total_mem = a[0]
users = a[1]

user_mem = []

i = 0
while i < users:
    user_mem.append(int(input()))
    i += 1
user_mem.sort()

j = 0
in_ar = 0
for s in user_mem:
    in_ar += s

    if in_ar <= total_mem:
        j += 1
    else:
        break

print(j)
