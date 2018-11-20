from time import time

t0 = time()

D = {1 : 0}


def fiter(n):
    x = n
    cnt = 0
    while x > 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        cnt += 1
        if x in D:
            cnt += D[x]
            break

    D[n] = cnt
    return cnt


def fre(n):
    if n in D:
        return D[n]
    if n % 2 == 0:
        n2 = n //2
    else:
        n2 = 3*n + 1

    res = fre(n2) + 1
    D[n] = res
    return res



m = 0
best = 1

for i in range(1, 100_000_001):
    val = fre(i)
    if val > m:
        best = i
        m = val

    #print(i, val)


print(best, m)
print('time = {} c'.format(time() - t0))