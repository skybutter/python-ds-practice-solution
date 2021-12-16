def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # res = {}
    # myphrase = phrase.lower()
    # for i in 'aeiou':
    #     if myphrase.count(i) > 0:
    #         res[i] = myphrase.count(i)
    # return res
    # Solution
    res = {}
    myphrase = phrase.lower()
    VOWELS = set('aeiou')
    for i in myphrase:
        if i in VOWELS:
            res[i] = res.get(i, 0) + 1
    return res


print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))