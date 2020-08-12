_ = int(input())
s = list(map(int, input().split()))
x = int(input())
a = [abs(x-i) for i in s]
print(s[a.index(min(a))])
