def dict_sort(q):
    return -q[0], q[1]


file = open("input.txt", mode="r", encoding="utf-8")

s = list(map(str.strip, file.readlines()))
d = dict()

for a in s:
    if d.__contains__(a):
        d[a] += 1
    else:
        d[a] = 1

results = []

lim = len(s) / 2

for da in d:
    das = (d[da], da)
    results.append(das)

results.sort(key=dict_sort)

file_r = open("output.txt", mode="w", encoding="utf-8")

print(results[0][1], file=file_r)
if results[0][0] <= lim:
    print(results[1][1], file=file_r)
file_r.close()
