def main():
    st = input().split('-')
    p = ''.join(st[0].split('.'))
    s = st[1]
    # print(p,s)
    st = ''.join(''.join(st).split('.'))
    i = 1
    while i < len(st) - 1:
        if st[i] == st[i-1]:
            i += 1
            continue
        else:
            break
    if i == len(st) - 1:
        return print("Nao")
    soma = 0
    i = 10
    for n in p:
        soma += int(n)* i
        i -= 1
        # print(soma)
    r = soma % 11
    # print(r)
    # (r < 2 and s[0] == 0) or not (r > 2 and s[0] == (11-r)):
    if r < 2:
        if s[0] != '0':
            # print("aqui")
            return print("Nao")
        p += '0'
    else:
        if s[0] != str(11-r):
            # print("aqui2")
            return print("Nao")
        p += str(11-r)
    
    soma = 0
    i = 11

    for n in p:
        soma += int(n)* i
        i -= 1
        # print(soma, n, i)
    r = soma % 11
    # print(r)
    if r < 2:
        if s[0] != '0':
            # print("aqui")
            return print("Nao")
        p += '0'
    else:
        if s[0] != str(11-r):
            # print("aqui2")
            return print("Nao")
        p += str(11-r)
    print("Sim")
main()