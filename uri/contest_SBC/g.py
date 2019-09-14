import math as m

v,n = map(int, input().split())

total = v * n
ans = []

for i in range(1,10):
    aux = total * (i/10)
    aux = m.ceil(aux)
    ans.append(int(aux))

for i in range(len(ans)-1):
    print(ans[i], end=' ')
print(ans[-1])