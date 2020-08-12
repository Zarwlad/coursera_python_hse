a = int(input())

line1 = "+___ "
line3 = "|__\\ "
line4 = "|    "

line2List = []

i = 1
while i <= a:
    line2 = "|%d / " % i
    line2List.append(line2)
    i += 1

print(line1 * a)
for b in line2List:
    print(b, end="")
print()
print(line3 * a)
print(line4 * a)
