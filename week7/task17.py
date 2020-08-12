file = open("input.txt", mode="r", encoding="utf8")

s = list(map(str, file.read().split()))

d = dict()
mx = 0

for a in s:
    if d.__contains__(a):
        d[a] += 1
    else:
        d[a] = 1
    if d[a] > mx:
        mx = d[a]

results = []

for da in d:
    if d[da] == mx:
        results.append(da)

results.sort()
print(results[0])
