def cup_of_join_5_2(*parameters, sep='-'):
    if not parameters:
        return None
    res = []
    for par in parameters:
        for i in par:
            res.append(i)
        res.append(sep)
    res.pop()
    print(res)