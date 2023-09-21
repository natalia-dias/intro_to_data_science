scores = input().split()
c = 0
ic = 0
for i in scores:
    if ic == 3:
        break
    elif i == 'C':
        c += 1
    elif i == "I":
        ic += 1

if ic == 3:
    print("Game over")
else:
    print("You won")
print(c)
