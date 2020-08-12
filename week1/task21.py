kms_per_day = int(input())
total_kms = int(input())

total_days = (total_kms - 1) // kms_per_day + 1

print(total_days)
