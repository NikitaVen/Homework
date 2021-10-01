names = []
try:
    input_file = open("data/unsorted_names.txt")
    names = input_file.read().split()
    if len(names) == 0:
        raise Exception(input_file.name + " is empty")
    input_file.close()
    names.sort()
    output_file = open("data/sorted_names.txt", "w")
    for name in names:
        output_file.write(name + '\n')
    output_file.close()
except Exception as ex:
    print(ex)
    exit(-1)
print("names are sorted")




