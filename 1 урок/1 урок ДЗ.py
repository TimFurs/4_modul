def is_str_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

print(is_str_palindrome('TACOCAT'))
print(is_str_palindrome('HELLO'))


