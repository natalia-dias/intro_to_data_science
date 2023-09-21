# put your python code here
check = 0
sum_numb = 0
sum_sqr = 0
while True:

    numb = int(input())
    sum_numb += numb
    sum_sqr += numb ** 2
    if sum_numb == check:
        print(sum_sqr)
        break