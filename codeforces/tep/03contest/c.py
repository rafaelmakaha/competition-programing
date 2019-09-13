def main():
    n = int(input())

    st = input()
    
    if n < 2:
        return st

    st = [x for x in st]

    ans = ""

    if n % 2 == 0:
        aux = True
    else:
        aux = False

    for i in range(n):
        if len(st) == 0:
            break
        if aux:
            ans = st.pop(0) + ans
            aux = not aux
        else:
            ans = ans + st.pop(0)
            aux = not aux
        # ans = ans[:(len(ans)//2) + 1] + st.pop(0) + ans[(len(ans)//2)+1:]

    return ans

print(main())