first = int(input())
sec = int(input())

yes = "YES"
no = "NO"

remind = first % sec

c = 0 ** remind
# 0**0 = 1
# в любых других степенях - 0

print(yes * c, no * (1 - c))
