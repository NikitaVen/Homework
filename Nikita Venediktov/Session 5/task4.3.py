def get_top_performers(file_path, number_of_top_students=5):
    input_file = open(file_path)
    array = []
    input_file.readline()
    for line in input_file:
        temp = line.split(sep=",")
        if len(temp) < 3:
            raise Exception("wrong format")
        array.append((temp[0], float(temp[2])))
    input_file.close()
    array.sort(key=lambda x: x[1], reverse=True)
    res = []
    for index, value in enumerate(array):
        if index >= number_of_top_students:
            break
        res.append(value[0])
    return res


def write_records_in_descending_order_of_age(input_file_path, output_file_path):
    input_file = open(input_file_path)
    array = []
    starting = input_file.readline()
    for line in input_file:
        temp = line.split(sep=",")
        if len(temp) < 3:
            raise Exception("wrong format")
        array.append((temp[0], int(temp[1]), temp[2]))
    input_file.close()
    array.sort(key=lambda x: x[1], reverse=True)
    output_file = open(output_file_path, "w")
    output_file.write(starting)
    for line in array:
        output_file.write(line[0] + ',' + str(line[1]) +',' + line[2])
    output_file.close()



try:
    print(get_top_performers("data/students.csv"))
    write_records_in_descending_order_of_age("data/students.csv", "data/sorted_students.csv")
except Exception as ex:
    print(ex)

