def main():
    n = int(input())

    count = 0

    for i in range(n):
        q = map(int, input().split())
        if sum(q) >= 2:
            count += 1
    print(count)

main()