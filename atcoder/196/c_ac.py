N = int(input())
ans = 0

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        tmp = str(int(str(a) + str(b) + str(c) + str(d) + str(e) + str(f)))
                        tmp += tmp
                        tmp = int(tmp)
                        if tmp <= N:
                            if tmp:
                                ans += 1
                        else:
                            print(ans)
                            exit()

print(ans)
