
def most_common_words(filepath, number_of_words=3):
    input_file = open(filepath)
    dic = {}
    words = input_file.read().split()
    input_file.close()
    for word in words:
        if word not in dic.keys():
            dic[word] = 1
        else:
            dic[word] += 1
    sorted_words = []
    for key, value in dic.items():
        sorted_words.append((value, key))
    sorted_words.sort(reverse=True)
    res = []
    for index, value in enumerate(sorted_words):
        if index >= number_of_words:
            break
        res.append(value[1])
    return res



try:
    print(most_common_words("data/lorem_ipsum.txt"))
except Exception as ex:
    print(ex)
