stave = int(input())
up = int(input())
down = int(input())

m_per_day = up - down

st_days = (stave - up - 1) // m_per_day + 1 + 1

print(st_days)
# за последний день
# улитка пройдет весь up
# поэтому уменьшаем stave
# на up
# и гарантированно добавляем 1
