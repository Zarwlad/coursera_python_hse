string = str(input())

s = string.split()

nums = []

for sa in s:
    nums.append(int(sa))

nums.sort(reverse=True)

less_positive = 5000

for n in nums:
    if 0 < n < less_positive:
        less_positive = n
    if n <= 0:
        break

print(less_positive)
