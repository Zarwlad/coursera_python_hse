string = str(input())

s = string.split()

positives = []

for sas in s:
    sas = int(sas)
    if sas > 0:
        positives.append(sas)

print(len(positives))
