
def swapQuotes(s: str):
    if not s:
        return None
    res = ""
    for character in s:
        temp = character
        if character == '\"':
            temp = '\''
        elif character == '\'':
            temp = '\"'
        res += temp
    return res



s = " Hello \' Bye \" Hi See you\'"

print(swapQuotes(s))
