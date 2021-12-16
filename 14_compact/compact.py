def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # lst_new = []
    # for i in lst:
    #     if i:
    #         lst_new.append(i)
    # return lst_new
    # Solution
    return [val for val in lst if val]


print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
