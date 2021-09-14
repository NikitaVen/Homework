
dick = {}
while True:
    temp_key = input("Enter the key(ex to exit): ")
    temp_key_str = temp_key.strip()
    if temp_key_str == "":
        continue
    if temp_key.strip() == "ex":
        break
    temp_value = input("Enter the value: ")
    dick[temp_key.strip()] = temp_value.strip()

dick_items = dick.items()
sorted_items = sorted(dick_items)
print("Sorted dictioanry: ", end="")
for item in sorted_items:
    if sorted_items.index(item) == len(sorted_items) - 1:
        print(str(item[0]) + ": " + item[1])
    else:
        print(str(item[0]) +  ": " + item[1], end=', ')