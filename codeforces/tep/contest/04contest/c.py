def main():

    st = input()

    ans = ""
    leng = len(st)
    st = [c for c in st]
    # print(st)
    if leng == 1 or (leng == 2 and st[0] != st[1]):
        return print(''.join(st))
    elif leng == 2 and st[0] == st[1]:
        st[0] = chr(ord(st[1])+1)
        return print(''.join(st))
    elif leng == 3:
        if st[0] == st[1] and st[1] == st[2]:
            st[1] = chr(ord(st[1])+1)
        elif st[0] == st[1]:
            st[0] = chr(ord(st[0]) +1)
        elif st[1] == st[2]:
            st[2] = chr(ord(st[2]) +1)
        else:
            return print(''.join(st))            
    else:
        for i in range(leng - 1):
            p = st[i: i + 2]
            n = chr(ord(st[i])+1)
            # print(p, n, st, i, leng)
            if p[0] != p[1]:
                continue
            if p[0] == p[1] and i == 0:
                st[i+1] = n
            elif p[0] == p[1] and i != leng -2:
                if st[i+2] == n:
                    n = chr(ord(n) + 1)
                st[i + 1] = n
            else:
                st[i+1] = n
    return print(''.join(st))       


# main()

st = input()

ans = ""

len = len(st)

