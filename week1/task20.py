hours1 = int(input())
mins1 = int(input())
secs1 = int(input())
hours2 = int(input())
mins2 = int(input())
secs2 = int(input())

secs_total1 = hours1 * 3600 + mins1 * 60 + secs1
secs_total2 = hours2 * 3600 + mins2 * 60 + secs2

print(secs_total2 - secs_total1)
