def remember_results(f, res=None):
    last = None
    def func(*args):
        nonlocal last
        print("Last result: " + str(last))
        res = f(*args)
        last = res
        return res
    return func



@remember_results
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result


sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)