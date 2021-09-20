def foo(l):
    res= []
    for index,value in enumerate(l):
        temp = 1
        for index_2, value_2 in enumerate(l):
            if index_2 != index:
                temp *= value_2
        res.append(temp)
    return res

print(foo([1, 2, 3, 4, 5]))
print(foo([3, 2, 1]))