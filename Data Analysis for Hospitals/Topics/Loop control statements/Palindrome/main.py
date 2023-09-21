palindrome = "Palindrome"
not_palindrome = "Not palindrome"


def check_if_palindrome(string):
    if string == string[::-1]:
        return palindrome
    return not_palindrome


print(check_if_palindrome(input()))
