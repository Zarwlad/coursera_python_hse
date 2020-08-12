secs_input = int(input())

hours = (secs_input // 3600) % 24
mins = ((secs_input // 60) % 60)
secs = (secs_input % 60)

min_f_d = mins // 10
min_s_d = mins % 10

sec_f_d = secs // 10
sec_s_d = secs % 10

print(hours, ":", min_f_d, min_s_d, ":", sec_f_d, sec_s_d, sep="")
