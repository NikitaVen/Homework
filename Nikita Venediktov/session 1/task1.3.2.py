
try:
    num = int(input("Enter integer number: "))
except:
    print("invalid data")
    exit(0)
arr = []
for i in range(1, abs(int(num / 2) + 1)):
    if num % i == 0:
        arr.append(i)
arr.append(abs(num))
print("Integer dividers of " + str(num) + ": ", end = "")
for i in arr:
    print(str(i), end=" ")
print("\n")
