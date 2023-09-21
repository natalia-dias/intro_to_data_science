line_input = str(input())
vowels = ['a', 'e', 'i', 'o', 'u']

for i in line_input:
    if i.isalpha():
        if i in vowels:
            print("vowel")
        else:
            print("consonant")
    else:
        break
