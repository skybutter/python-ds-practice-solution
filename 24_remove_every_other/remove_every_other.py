def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    # cnt = 1
    # newlist = []
    # for i in lst:
    #     if cnt % 2 == 1:
    #         newlist.append(i)
    #     cnt = cnt + 1
    # return newlist
    # Solution 1
    # return [val for i,val in enumerate(lst) if i%2==0]
    # Solution 2
    return lst[::2]

lst = [1, 2, 3, 4, 5]
print(remove_every_other(lst))
print(lst)
