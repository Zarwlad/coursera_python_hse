string = str(input())

s = string.split()

biggers = []
i = 0

for sas in s:
    if i != 0:
        sas = int(sas)
        sas_prev = int(s[i-1])
        if sas > sas_prev:
            biggers.append(sas)
    i += 1

print(" ".join(map(str, biggers)))
