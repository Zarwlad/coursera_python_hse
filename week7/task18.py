def sort_com(la):
    return -la[0], la[1]


file = open("input.txt", mode="r", encoding="utf8")

s = list(map(str, file.read().split()))
d = dict()

for a in s:
    if d.__contains__(a):
        d[a] += 1
    else:
        d[a] = 1

results = []

for da in d:
    a = (d[da], da)
    results.append(a)

results.sort(key=sort_com)

for result in results:
    print(result[1])
