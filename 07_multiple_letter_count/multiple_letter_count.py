def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # dic = {}
    # for c in phrase:
    #     if c in dic.keys():
    #         dic[c] = dic[c] + 1
    #     else:
    #         dic[c] = 1
    # return dic
    counter = {}
    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1
    return counter


print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))
