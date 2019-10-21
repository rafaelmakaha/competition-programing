n = int(input())

for _ in range(n):
    m = int(input())
    st = input()
    st_r = ""
    if st.count('8') == 0:
        print("NO")
    elif len(st) == 11 and st[0] != '8':
        print("NO")
    elif len(st) < 11:
        print("NO")
    elif len(st[st.find('8'):]) >= 11:
            print("YES")
    else:
        print("NO")