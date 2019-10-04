n = int(input())
st = input()

result = ""
maior = 0

for i in range(n-1):
    # a = st.count(st[i:i+2])
    count = 0
    for j in range(n-1):
        if st[j:j+2] == st[i:i+2]:
            count += 1
    
    # print(st[i:i+2], count)
    if count > maior:
        maior = count
        result = st[i:i+2]

print(result)