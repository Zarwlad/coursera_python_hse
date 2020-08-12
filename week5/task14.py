string = str(input())

s = string.split()

evens = []

for sas in s:
    sas = int(sas)
    if sas % 2 == 0:
        evens.append(sas)

for e in evens:
    print(e, end=" ")
