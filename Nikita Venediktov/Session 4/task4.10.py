
def generateSquares(num):
    d = {}
    if not num or num <= 0:
        return None
    d = {}
    for i in range(num + 1)[1:]:
        d[i] = i**2
    return d

print(generateSquares(5))