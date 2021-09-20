def get_longest_word(s: str) -> str:
    if not s:
        return ""
    longest = ""
    start = 0
    index = 0
    for index, value in enumerate(s):
        if not value.isspace():
            start = index
            while index < len(s) and not s[index].isspace():
                index += 1
            if len(s[start:index]) > len(longest):
                longest = s[start:index]
    return longest



print(get_longest_word('Python is simple and effective!'))
print(get_longest_word('Any pythonista like namespaces a lot.'))
print(get_longest_word("Hello      everybody \n My name is Tyler"))
