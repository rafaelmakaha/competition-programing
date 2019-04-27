import itertools

def main():
    x = int(input())
    lst = input()

    azip = list(itertools.product([0, 5], repeat=x))
    # azip = list(zip(*a))
    print(azip)
    out = list(zip(map(int, azip[0]), azip[1], azip[2], azip[3]))
    # lst = filter(lambda x: x.count(5) ==10, lst)

main()