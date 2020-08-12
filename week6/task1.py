def merge(A, B):
    c = A + B
    cs = sor(c)
    return cs


def sor(l):
    ls = sorted(l)
    return ls


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = merge(a, b)
print(*c)
