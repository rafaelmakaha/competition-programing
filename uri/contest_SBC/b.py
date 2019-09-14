def main():
    n = int(input())
    carlos = int(input())
    
    for _ in range(n-1):
        if int(input()) > carlos:
            flag = True

    if flag:
        return "N"
    return "S"

print(main())