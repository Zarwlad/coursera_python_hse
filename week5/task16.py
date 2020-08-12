string = str(input())

s = string.split()

maxi = -100_000_000
max_ind = 0
i = 0

for sas in s:
    sas = int(sas)
    if sas >= maxi:
        maxi = sas
        max_ind = i
    i += 1

print(maxi, max_ind)
