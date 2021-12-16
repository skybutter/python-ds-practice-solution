def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # lphrase = phrase.replace(' ', '').lower()
    # length = len(lphrase)
    # x = 1
    # for c in lphrase:
    #     if x >= (length/2):
    #         return True
    #     if c != lphrase[length-x]:
    #         return False
    #     else:
    #         x = x + 1
    normalize = phrase.lower().replace(' ', '')
    return normalize == normalize[::-1]


print(is_palindrome('tacocat'))
print(is_palindrome('noon'))
print(is_palindrome('robert'))
print(is_palindrome('taco cat'))
print(is_palindrome('Noon'))
