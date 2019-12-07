def main():
    st = input()
    s =  set(st)
    # print(len(s),len(st)//2)
    # if len(st) % 2 == 0:
    #     if len(s) > len(st)//2:
    #         print("Nao")
    #     else:
    #         print("Sim")
    # else:
    #     if len(s) > 1+len(st)//2:
    #         print("Nao")
    #     else:
    #         print("Sim")
    dic = {}
    for c in s:
        dic[c] = st.count(c)
    par = 0
    imp = 0
    for key in dic.keys():
        if dic[key] % 2 == 0:
            par += 1
        else:
            imp += 1
    if imp > 1:
        return print('Nao')
    else:
        return print('Sim')

main()