def get_matrix(a, b, c):
    result = []
    inside = []
    for i in range(b):
        inside.append(c)
    for k in range(a):
        result.append(inside)
    return result

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
