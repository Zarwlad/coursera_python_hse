miD = dict()

nums = int(input())
lines = []

for s in range(nums):
    lines.append(input())

for l in lines:
    ls = list(map(str, l.split()))
    miD[ls[0]] = ls[1]
    miD[ls[1]] = ls[0]

b = str(input())
print(miD[b])
