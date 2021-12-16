def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    # Method 1
    # count = 0
    # for i in lst:
    #     if i == search_term:
    #         count = count + 1
    # return count
    # Method 2
    # return lst.count(search_term)
    # Method 3
    from collections import Counter
    d = Counter(lst)
    return d[search_term]


print(frequency([1, 4, 3, 4, 4], 4))
print(frequency([1, 4, 3], 7))
