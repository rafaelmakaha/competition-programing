def main():
    n = int(input())
    lst = list(map(int, input().split()))
    
    pages_read = 0

    while pages_read < n:
        i = 1
        while i-1 < len(lst):
            pages_read += lst[i-1]
            if pages_read >= n:
                break
            else:
                i+=1
    print(i)


main()
