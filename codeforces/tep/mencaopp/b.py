def main():
    n = int(input())
    ans = []
    for j in range(n):
        st = input().lower()
        ans.append('Errada')
        if not 'p' in st and not 'b' in st:
            ans[j] = 'Certa'
            continue
        if st.find('p') == 0 or st.find('b') == 0:
            ans[j] = 'Errada'
            continue
        for i in range(len(st)):
            if i != 0 and( st[i] == 'p' or st[i] == 'b'):
                if st[i-1] == 'm':
                    ans[j] = 'Certa'
                else:
                    ans[j] = 'Errada'
                    break

    for a in ans:
        print(a)

main()