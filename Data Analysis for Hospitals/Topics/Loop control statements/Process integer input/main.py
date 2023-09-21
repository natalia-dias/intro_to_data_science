list_numb = []
while True:
    a = int(input())
    if a < 10:
        continue
    elif a > 100:
        break
    else:
        list_numb.append(a)

for i in list_numb:
    print(i)
