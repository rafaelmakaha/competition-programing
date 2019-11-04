def main():
    a = input()
    b = input()

    voyals = ['a', 'e', 'i', 'o', 'u']

    if len(a) != len(b):
        return print("No")

    for i in range(len(a)):
        if a[i] in voyals and b[i] in voyals:
            continue
        elif not a[i] in voyals and not b[i] in voyals:
            continue
        else:
            return print("No")
    print("Yes")

main()