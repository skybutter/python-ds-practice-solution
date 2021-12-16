def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # My method
    # swapped = ''
    # for c in phrase:
    #     if c.lower() == to_swap.lower():
    #         if c.isupper():
    #             swapped = swapped + c.lower()
    #         else:
    #             swapped = swapped + c.upper()
    #     else:
    #         swapped = swapped + c
    # return swapped
    # Solution
    out = ''
    for ltr in phrase:
        if ltr.lower() == to_swap.lower():
            ltr = ltr.swapcase()
        out += ltr
    return out


print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))
