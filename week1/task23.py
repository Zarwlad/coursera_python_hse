number = int(input())
leftPart = number // 100
rightPart = ((number % 10) * 10) + ((number // 10) % 10)
print((leftPart - rightPart + 1)**2)
