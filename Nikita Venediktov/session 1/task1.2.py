
def characters_frequency(str):
    d = dict()
    for i in str:
       if i.casefold() in d:
           d[i.casefold()] += 1
       else:
           d[i.casefold()] = 1
    return d

while(True):
    temp = str(input("Enter your string(ex to exit): "))
    if temp.strip() == "ex":
        break
    else:
        d = characters_frequency(temp)
        print("Characters frequency: ")
        for i, value in d.items():
            print(str(i) + ': ' + str(value))