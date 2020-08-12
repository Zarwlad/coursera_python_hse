num = float(input())

f_num_dig = int((num - int(num)) * 10)

if f_num_dig >= 5:
    num = int(num) + 1
else:
    num = int(num)

print(num)
