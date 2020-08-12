cost_rub = int(input())
cost_cop = int(input())
qty = int(input())

cost = cost_rub * 100 + cost_cop
cost_per_qty = cost * qty

print(cost_per_qty // 100, cost_per_qty % 100)
