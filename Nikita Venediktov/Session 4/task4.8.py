def get_pairs(lst: list):

    if not lst or len(lst) == 1:
        return None
    res= []
    for index, value in enumerate(lst):
        if index != len(lst) - 1:
            res.append((value, lst[index + 1]))
    return res


print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))