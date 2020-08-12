percent = int(input())
rub = int(input())
cop = int(input())

depo = cop + rub * 100
end_year = depo + depo * (percent/100)

end_rub = int(end_year // 100)
end_cop = int(end_year % 100)

print(end_rub, end_cop)
