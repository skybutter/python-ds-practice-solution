def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    # out = ''
    # for ltr in phrase:
    #     ltr = ltr.upper()
    #     break
    # out = ltr + phrase[1:]
    # return out
    # Solution
    return phrase.capitalize()


print(capitalize('python'))
print(capitalize('only first word'))
