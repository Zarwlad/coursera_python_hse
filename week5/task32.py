nums = list(map(int, input().split()))

i = 1

while i < len(nums):
    prev = nums[i - 1]
    curr = nums[i]
    nums.__setitem__(i, prev)
    nums.__setitem__(i - 1, curr)
    i += 2

print(* nums)
