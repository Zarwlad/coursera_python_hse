col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

isColAllow = col2 == col1 or col2 == col1 - 1 or col2 == col1 + 1
isRowAllow = row2 == row1 or row2 == row1 - 1 or row2 == row1 + 1

if isColAllow and isRowAllow:
    print("YES")
else:
    print("NO")
