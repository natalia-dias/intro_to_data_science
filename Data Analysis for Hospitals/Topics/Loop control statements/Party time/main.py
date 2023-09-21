guest_list = []
while True:
    name = input()
    if name == '.':
        break
    guest_list.append(name)
print(guest_list)
print(len(guest_list))
