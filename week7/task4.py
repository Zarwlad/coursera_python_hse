nums = list(map(int, input().split()))

setT = set()

for num in nums:
    if setT.__contains__(num):
        print("YES")
    else:
        print("NO")
    setT.add(num)
