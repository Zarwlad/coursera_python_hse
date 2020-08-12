def min4(a, b, c, d):
    ab_min = min(a, b)
    cd_min = min(c, d)
    return min(ab_min, cd_min)


a, b = int(input()), int(input())
c, d = int(input()), int(input())

print(min4(a, b, c, d))
