mean = 0
vol = 0
while True:
    user_input = input()
    if user_input != ".":
        mean += int(user_input)
        vol += 1
    else:
        break

the_mean = mean / vol

print(the_mean)
