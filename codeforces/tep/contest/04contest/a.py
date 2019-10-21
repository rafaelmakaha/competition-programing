f = input()
s = input()

st = input()
ans = ""

for c in st:
    i = f.find(c.lower())
    if c.isnumeric():
        ans = ans + c        
    elif c.isupper():
        ans = ans + s[i].upper()
    else:
        ans = ans + s[i].lower()

print(ans)