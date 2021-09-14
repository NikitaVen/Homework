
arr = []
while True:
    try:
        temp = input("Enter positive integer(ex to exit): ")
        if temp.strip() == "ex":
            break
        temp = int(temp)
        if temp <= 0:
            raise Exception
        arr.append(temp)
    except:
        print("invalid input")
        continue
arr = tuple(arr)
s = ""
for num in arr:
    s += str(num)
if len(s) != 0:
    rez = int(s)
    print("The number is " + str(rez))
else:
    print("tuple is empty")


