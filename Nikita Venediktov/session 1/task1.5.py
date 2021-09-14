l = []
i = 1
while True:
    print("ENTER " + str(i) + " DICTIONARY:")
    temp_dic = {}
    while True:
        temp_key = input("Enter the key(ex to exit): ")
        temp_key_str = temp_key.strip()
        if temp_key_str == "":
            continue
        if temp_key.strip() == "ex":
            break
        temp_value = input("Enter the value: ")
        temp_dic[temp_key.strip()] = temp_value.strip()
    if len(temp_dic) != 0:
        l.append(temp_dic)
    answer  = input("---------------------\nDo you want to add one more dictionary(y/n)? ")
    if answer.strip() == "n":
        break
    i += 1

s = set()
for i in l:
    for j in i.values():
        s.add(j)
print("Unique values: ", end='')
for i in s:
    print(str(i), end=" ")