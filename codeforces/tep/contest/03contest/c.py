st = input()

if st.isupper() or (st[0].islower() and st[1:].isupper()) :
    print(st.swapcase())
elif len(st) == 1:
    print(st.swapcase())
else:
    print(st)