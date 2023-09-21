profit = [(i - j) for i, j in zip(revenues, costs)]
for mon, prof in zip(months, profit):
    print(mon, prof)
