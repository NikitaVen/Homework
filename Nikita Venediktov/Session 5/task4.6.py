def call_once(f):
    res = [False, None]
    def func(a, b):
        nonlocal res
        if not res[0]:
            res[0] = True
            res[1] = f(a, b)
        return res[1]
    return func




@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))