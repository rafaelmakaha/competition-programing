import math 

def findIndex(n) : 
    fibo = 2.078087 * math.log(n) + 1.672276
    return round(fibo) 

def binet(n):
    phi = (1 + 5**0.5) / 2
    psi = (1 - 5**0.5) / 2
    return (phi**n - psi**n) / 5**.5

def main():
    
    x = int(input())

    index = findIndex(x)

    if x < 1:
        print("I'm too stupid to solve this problem")
    elif x == 1:
        print("0 0 1")
    else:
        print(int(binet(index - 4)), int(binet(index - 3)), int(binet(index - 2)))

main()
