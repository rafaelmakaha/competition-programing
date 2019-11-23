def main():
    x = input().split()
    n,m = x
    n = int(n)
    m = int(m)

    st = input()
    buff = []
    aux = 0
    
    if m == n:
        return print(0)

    for index,c in enumerate(st):
        if not c in buff:
            buff.append(c)
        else:
            aux = index 
            break
        if index == n -1 :
            aux = n
    #     print(index, c, buff)
    # print("aux: " ,aux)
    ans = aux - m
    # print(ans)
    if ans < 0:
        print(0)
    else:
        print(ans)

main()
