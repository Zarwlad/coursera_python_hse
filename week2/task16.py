a, b, c = int(input()), int(input()), int(input())
matches = 0

if a == b:
    matches = matches + 1
if a == c:
    matches = matches + 1
if b == c:
    matches = matches + 1

if matches == 1:
    matches = matches + 1

print(matches)
