nums = []

inputs = int(input())

while inputs != 0:
    nums.append(inputs)
    inputs = int(input())

nums.sort()
print(nums[-2])
