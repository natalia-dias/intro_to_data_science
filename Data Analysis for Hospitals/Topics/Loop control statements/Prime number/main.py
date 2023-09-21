# num = int(input())
#
# # define a flag variable
# flag = False
#
# if num == 1:
#     print('This number is not prime')
# elif num > 1:
#     # check for factors
#     for i in range(2, int(num / 2)):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break
#
#     # check if flag is True
#     if flag:
#         print('This number is not prime')
#     else:
#         print('This number is prime')
answer = 0
for i in range(1, 101):
    answer += i

print(answer)
