import math

def main():
    n, c, t = map(int,input().split())
    q = [int(x) for x in input().split()]

    time = 0
    while any(q) and time < 51:
        flag = True
        visitados = [0] * n
        count = c
        time += 1
        i = 0
        while i != n:
            if not count:
                break
            elif flag:
                if q[i] < 1:
                    flag = not flag
                    continue
                else:
                    if visitados[i]:
                        i += 1
                        continue
                    visitados[i] = 1
                    q[i] = q[i] - t
                    q[i] = max(q[i], 0)
                    count -= 1
                    i += 1 
                    flag = not flag
            else:
                if q[-i] < 1:
                    i += 1
                    continue
                else:
                    if visitados[-i]:
                        i += 1
                        flag = not flag
                        continue
                    visitados[-i] = 1
                    q[-i] = q[-i] - t
                    q[-i] = max(q[-i], 0)
                    count -= 1
                    i += 1 
                    flag = not flag
        
        
    print(time)

main()