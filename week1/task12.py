minutes_input = int(input())

hours = (minutes_input // 60) % 24
minutes = (minutes_input % 60) % 1440

print(hours, minutes)
