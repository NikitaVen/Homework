import string

def commonCharacters(*strings):
    res = set()
    if not len(strings) or not strings[0]:
        return res
    for character in strings[0]:
        toAdd = True
        if len(strings) == 0:
            res.add(character)
        else:
            for s in strings[1:]:
                if not s:
                    return set()
                if not character in s:
                    toAdd = False
                    break
            if toAdd:
                res.add(character)
    return res

def allCharacters(*strings):
    res = set()
    for s in strings:
        if s is not None:
            for character in s:
                res.add(character)
    return res

def twoStringsCharacters(*strings):
    arr = []
    if not len(strings):
        return set()
    for s in strings:
        if s is not None:
            temp = set()
            for character in s:
                temp.add(character)
            arr.append(temp)
    res = {}
    for word in arr:
        for character in word:
            if not character in res:
                res[character] = 1
            else:
                res[character] += 1
    del arr
    s = set()
    for character, amount in res.items():
        if amount >= 2:
            s.add(character)
    return s


def unusedLetters(*strings):
    letters = list(string.ascii_lowercase)
    for s in strings:
        if s is not None:
            for character in s:
                if character.casefold() in letters:
                    letters.remove(character.casefold())
    return letters





s = ["hello", "world", "python"]
print(commonCharacters(*s))
print(allCharacters(*s))
print(twoStringsCharacters(*s))
print(unusedLetters(*s))


