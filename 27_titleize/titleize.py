def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # res = ''
    # for i in range(len(phrase)):
    #     if i == 0:
    #         res = phrase[i].upper()
    #     elif i > 0 and phrase[i-1] == ' ':
    #         res = res + phrase[i].upper()
    #     else:
    #         res = res + phrase[i].lower()
    # return res
    # Solution 1
    # return phrase.title()
    # Solution 2
    return ' '.join([val.capitalize() for val in phrase.split(' ')])


print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))