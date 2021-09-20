
def combineDicts(*dicts):
    res = {}
    for d in dicts:
        if d:
            for key, value in d.items():
                if key in res:
                    res[key] += value
                else:
                    res[key] = value
    return res

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combineDicts(dict_1, dict_2, dict_3))