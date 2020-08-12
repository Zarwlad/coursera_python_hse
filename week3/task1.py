import math

num1 = float(input())
num2 = float(input())
num3 = float(input())

halfP = (num1 + num2 + num3)/2

square = math.sqrt(halfP * (halfP - num1) * (halfP - num2) * (halfP - num3))
print(square)
