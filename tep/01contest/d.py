s = map(int, input().split())
m, st = s

s = [i for i in str(st)]
soma = 0
for i in s:
    soma = soma + int(i)

menor = str(soma)
maior = str(soma)

for i in range(1,m):
    menor = menor + '9'
    maior = '9' + maior

if st == 0:
    print("-1 -1")
else:
    print(menor, maior)