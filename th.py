from threading import Thread
import time


def long(n, t, name='def'):
    print('Start'+ name)
    for i in range(n):
        print(name, i)
        time.sleep(t)
    print('End' + name)


t1 = Thread(target=long, args=(7, 1, 't1'))
t1.start()

t2 = Thread(target=long, args=(20, 0.5, 't2'))
t2.start()

t1.join()

print('END')