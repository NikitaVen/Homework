
def splitByIndex(s: str, indexes: list):
    if not s:
        return None
    if indexes == None:
        return [s]
    res = []
    indexes.sort()
    while len(indexes) > 0 and indexes[0] < 0:
        indexes.pop(0)
    index = 0
    index_of_index = 0
    start = 0
    while index < len(s) and index_of_index < len(indexes):
        if index == indexes[index_of_index]:
            index_of_index += 1
            res.append(s[start:index])
            start = index
        index += 1
    res.append(s[start:len(s)])
    return res

print(splitByIndex("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))