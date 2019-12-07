def main():
    st = input()
    ans = []
    a = 1
    i = 0
    if st == 'x':
        return print("Comando 1: (x)1")
    elif st == 'ox':
        return print("Comando 1: (ox)1")
    while i < len(st):
        # print(ans)
        if st[i] == 'x':
            p = i
            while st[p] == 'x':
                p +=1
            ans.append('Comando ' + str(a) + ': (x)' + str(p-i))
            a += 1
            i = p
            continue

        elif st[i] == 'o':
            p = i
            while st[p:p+2] == 'ox':
                p += 2
            ans.append('Comando ' + str(a) + ': (ox)' + str((p - i)//2))
            a += 1
            i = p
            continue

        elif st[i] == '.':
            p = i + 1
            while st[p] != '.':
                p += 1
            ans.append('Comando ' + str(a) + ': (.)[' + ''.join(st[i:p+1].split('.')) + ']')
            a += 1
            i = p + 1
            continue

    for k in ans:
        print(k)

if __name__ == "__main__":
    main()