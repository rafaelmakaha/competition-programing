def main():
    n = int(input())
    ans = []

    for i in range(n):
        v = [int(x) for x in input().split()]
        # print(v)
        if v[3] == 0:
            ans.append("YES")
        elif v[0] == 0 and v[1] == 0:
            ans.append("NO")
        else:
            r = v[3] % v[2]
            q = v[3] // v[2]
            if v[0] >= q and v[1] >= r:
                ans.append("YES")
            elif v[0] >= q and v[1] < r:
                ans.append("NO")
            else:
                k = v[3] - (v[0] * v[2])
                if v[1] >= k:
                    ans.append("YES")
                else:
                    ans.append("NO")
    for a in ans:
        print(a)
main()