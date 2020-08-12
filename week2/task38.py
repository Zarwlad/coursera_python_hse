inputs = int(input())
max_num = 0
count = 0

while inputs != 0:
    if inputs > max_num:
        max_num = inputs
        count = 1
    elif inputs == max_num:
        count = count + 1
    inputs = int(input())

print(count)
