
def Split(s, sep =None, maxsplit=-1):
    currentsplit = maxsplit
    res = []
    if not s or maxsplit == 0:
        return [s]
    index = 0
    start = 0
    while index < len(s):
        if sep == None and s[index].isspace() or s[index] == sep:
            res.append(s[start:index])
            if currentsplit >= 0:
                currentsplit -= 1
            start = index + 1
        if currentsplit == 0:
            res.append(s[start:])
            break
        index += 1
    if start == 0:
        return [string]
    if currentsplit != 0:
        res.append(s[start:index + 1])
    if sep is None:
        index = 0
        while index != len(res):
            if len(res[index]) == 0:
                res.pop(index)
            else:
                index += 1

    return res





string = " Всем привет,\n Меня    зовут Никита, \t a вас как?  "
print(Split(string))
print(string.split())