def main():
    a = input()
    map = {
        'L': -1,
        'R': +1,
        'U': +1,
        'D': -1,
    }
    x = 0
    y = 0
    for c in a:
        if c in ['L','R']:
            x += map[c]
        else:
            y += map[c]
    # print(x,y)
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    if len(a) % 2 != 0:
        return print(-1)
    elif x == y:
        return print(x)
    else:
        return print( (x+y)//2 )
main()