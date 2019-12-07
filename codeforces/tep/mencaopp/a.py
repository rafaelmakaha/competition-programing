def main():
    st = input().split()
    m,b,r,st = st

    ans = int(m) * int(b)
    ans += int(r) * len(st)
    print(ans)

main()