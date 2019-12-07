def main():
    n = int(input())

    ans = []
    for _ in range(n):
        st = input()
        s =  set(st)
        if ' ' in s:
            s.remove(' ')
        # print(s)
        ans.append(len(s))

    for a in ans:
        print(a)

main()