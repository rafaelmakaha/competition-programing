'''
F. Insomnia cure
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
«One dragon. Two dragon. Three dragon», — the princess was counting. She had trouble falling asleep, and she got bored of counting lambs when she was nine.

However, just counting dragons was boring as well, so she entertained herself at best she could. Tonight she imagined that all dragons were here to steal her, and she was fighting them off. Every k-th dragon got punched in the face with a frying pan. Every l-th dragon got his tail shut into the balcony door. Every m-th dragon got his paws trampled with sharp heels. Finally, she threatened every n-th dragon to call her mom, and he withdrew in panic.

How many imaginary dragons suffered moral or physical damage tonight, if the princess counted a total of d dragons?

Input
Input data contains integer numbers k, l, m, n and d, each number in a separate line (1 ≤ k, l, m, n ≤ 10, 1 ≤ d ≤ 105).

Output
Output the number of damaged dragons.
'''

def main():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    count =0
    for i in range(1,d+1):
        flag = 0
        if not i%k and not flag:
            flag=1
            count+= 1
        elif not i%l and not flag:
            flag=1
            count+= 1
        elif not i%m and not flag:
            flag=1
            count+= 1
        elif not i%n and not flag:
            flag=1
            count += 1

    print(count)

main()