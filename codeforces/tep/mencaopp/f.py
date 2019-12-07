def main():
    l1 = input().split()
    l2 = input().split()
    S,E,s = l1
    D,K,h = l2
    ep = 0
    dia = 0
    hora = 0
    for i in range(int(D) * int(K)):
        st = input()
        if s[1:3] == st[1:3] and int(s[4:]) == int(st[4:] + 1):
            ep += 1


main()