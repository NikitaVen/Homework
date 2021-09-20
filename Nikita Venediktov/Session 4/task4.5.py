def get_digits(num: int):
    if not num:
        return tuple()
    num = str(num)
    res = []
    for d in num:
        if d.isdigit():
            res.append(int(d))
    return tuple(res)





num = 84358977540849
print(get_digits(num))
num = "dfuhgtucrm8457y78tvn4yv"
print(get_digits(num)) #but annotation: int