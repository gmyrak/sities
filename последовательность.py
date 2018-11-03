def function(n):
    x=n
    i=0
    while x>1:
        if x%2==0:
            x //= 2
        else:
            x=3*x+1
        i += 1
    return i

for k in range(1,1000):
    print(k,function(k))

