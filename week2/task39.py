inputs = int(input())
prev_num = inputs
count = 0

count_list = []

while inputs != 0:
    if inputs == prev_num:
        count = count + 1
    elif inputs != prev_num:
        prev_num = inputs
        count_list.append(count)
        count = 1
    inputs = int(input())
count_list.append(count)

count_list.sort()

print(count_list[-1])
