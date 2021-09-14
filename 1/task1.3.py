
arr = input("Enter a comma separated sequence of words: ").split(sep = ',')
if len(arr[-1].strip()) == 0:
    arr.pop(-1)
for i in range(len(arr)):
    arr[i] = arr[i].strip()
arr = sorted(list(set(arr)))
print(arr)






