def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    # res = [1]
    # for i in range(2, num+1):
    #     if num % i == 0:
    #         res.append(i)
    # return res
    # return [val+1 for val in range(num) if num % (val+1) == 0]
    # Solution 1
    # Solution 2



print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
print(find_factors(321421))
print(find_factors(36))
