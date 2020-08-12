start = int(input())
limit = int(input())
days = 1

while start < limit:
    start = start + 0.1 * start
    days = days + 1

print(days)
