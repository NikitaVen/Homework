


while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter b number: "))
        if a > b:
            print("a can't be greater than b")
            continue
        c = int(input("Enter c number: "))
        d = int(input("Enter d number: "))
        if c > d:
            print("c can't be greater than d")
            continue
        break
    except:
        print("invalid input")
        continue

digit_amount = len(str(max(abs(a), abs(b)) * max(abs(c), abs(d))))
table = []
temp = []
temp.append(' ')
for s in range(c, d + 1):
    temp.append(s)
table.append(temp)
for col in range(a, b + 1):
    temp = []
    temp.append(col)
    for s in range(c, d + 1):
        temp.append(col * s)
    table.append(temp)
print()
for s in table:
    for c in s:
        print(str(c).ljust(digit_amount + 2), end="|" + ' ' * (digit_amount + 1))
    print('\n'+'-' * (len(table[0]) *(2 * digit_amount +4) - digit_amount -1))