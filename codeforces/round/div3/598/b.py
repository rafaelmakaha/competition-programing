def main():
    q = int(input())
    ans = []
    for _ in range(q):
        n = int(input())
        st = [int(x) for x in input().split()]
        # menor = [n + 1]
        base = st
        k = n -1 
        while k > 0:
            r = 1
            for i in range(n):
                print(i, st, r, k)
                if st[i] == r:
                    if i != 0:
                        if st[i] < st[i-1]:
                            aux = st[i]
                            st[i] = st[i-1]
                            st[i-1] = aux
                            k -= 1
                    r += 1
            if k == n - 1:
                break
            if st == sorted(base):
                break

        ans.append(st)
    for a in ans:
        print(a)


main()