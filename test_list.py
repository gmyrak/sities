import time
import random

t0 = time.time()

LSET = set()
L = []
#LSET = []


for i in range(30_000):
    k = random.randint(1, 1_000_000)
    if not k in LSET:
        #LSET.append(k)
        LSET.add(k)
        L.append(k)


print('Time: {} c'.format(time.time() - t0))