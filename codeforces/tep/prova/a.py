def main():
    st = input()
    al = input()
    j = 0
    for i in range(len(st)):
        if st[i] == al[j]:
            j += 1
        if j == len(al):
            return print("Sim")    
    return print("Nao")


main()