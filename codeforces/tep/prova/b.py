def fat(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 6
    if x == 4:
        return 24
    if x == 5:
        return 120
    if x == 6:
        return 720
    if x == 7:
        return 5040
    if x == 8:
        return 40320
    if x == 9:
        return 362880
    if x == 10:
        return 3628800


def main():
    n = int(input())
    st = input()

    if n == 1:
        return print(0)
    if n == 2:
        return print(0)
    # if n == 3:
    #     return print(2)
    if n > 3:
        ans = fat(n-2) * (n-1) + n
        return print(ans)
    else:
        ans = fat(n-2) * (n-1)
        return print(ans)

main()