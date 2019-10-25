def solve():
    a = [x for x in input()]
    b = [x for x in input()]
    tam = len(a)
    if tam % 2 != 0:
        # print("aqui")
        return print("NO")
    if ''.join(a) == ''.join(b):
        return print("YES")
    mid = tam//2
    a1 = a[:mid]
    a2 = a[mid:]
    b1 = b[:mid]
    b2 = b[mid:]
    # print(a1,a2,b1,b2)
    if set(a1) == set(b1) and set(a2) == set(b2):
        return print("YES")
    elif set(a1) == set(b2) and set(a2) == set(b1):
        return print("YES")
    return print("NO")
solve()