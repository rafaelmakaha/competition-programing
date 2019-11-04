def main():
    _ = input()
    a = input()
    count = 0
    ans = ''
    x = len(a)
    while x > 0:
        c = a[0]

        ans += c
        a = a.replace(c,'',1)
        l = len(ans)
        count += 1
        # print(count,ans,a, x)

        if l <= x and ans in a[:l]:
            n = a.count(ans)
            a = a.replace(ans,'',1)
            aux = ans
            ans = ans + aux*n
            count += n

        x = len(a)
        
    print(count)

main()