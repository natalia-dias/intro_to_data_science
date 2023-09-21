import string

double_alphabet = dict.fromkeys(string.ascii_lowercase, 0)
for single in double_alphabet:
    double_alphabet[single] = single * 2
