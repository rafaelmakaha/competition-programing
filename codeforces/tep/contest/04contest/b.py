st = input()

ans = ""

dot = st.find('.')
ln = st[dot - 1]
dec = st[dot + 1]

if st == 0.0:
    ans = 0.0
elif int(ln) == 9:
    ans = "GOTO Vasilisa."
elif int(dec) >= 5:
    ans = int(st[0:dot]) + 1
else:
    ans = int(st[0:dot])

print(ans)