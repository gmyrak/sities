import time
import random

t0 = time.time()

LSET = set()
L = []
#LSET = []

'''
if type(LSET) == list:
    add = lambda n: LSET.append(n)
elif type(LSET) == set:
    add = lambda n: LSET.add(n)
'''

for i in range(30_000):
    k = random.randint(1, 1_000_000)
    if not k in LSET:
        #LSET.append(k)
        LSET.add(k)
        L.append(k)


print('Time: {} c'.format(time.time() - t0))