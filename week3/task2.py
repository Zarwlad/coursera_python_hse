num = int(input())

i = 1
sum = 0

while i <= num:
    sum = sum + 1/i**2
    i = i + 1

print(sum)
