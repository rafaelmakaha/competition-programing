def main():
    st = input()
    n = len(st)

    count = 0

    for i in range(n//2):
        if st[i] == st[n-1-i]:
            continue
        else:
            count += 1
        if count > 1:
            return "NO"
    if count == 1:
        return "YES"
    elif count == 0 and n %2 != 0:
        return "YES"
    else:
        return "NO"

print(main())