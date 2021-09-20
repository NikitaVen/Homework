

def isPalindrom(s):
    if not s:
        return None
    s = s.strip().lower()
    index = 0
    while index <= len(s) / 2 - 1:
        if s[index] != s[len(s) - 1 - index]:
            return False
        index += 1
    return True



array = ["11/11/11", "Лепс спел ", "madAm", "racecar", "Python"]
print("Palindromes: ")
for string in array:
    print(string + " :" + str(isPalindrom(string)))
