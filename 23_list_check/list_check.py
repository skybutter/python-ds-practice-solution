def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # for i in lst:
    #     if not isinstance(i, list):
    #         return False
    # return True
    # Solution
    return all( isinstance(item, list) for item in lst )


print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))