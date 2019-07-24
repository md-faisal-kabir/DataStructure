def increse_factor(n):
    k=1
    a=[]
    while k*k < n:
        if n%k==0:
            yield k
            a.append(n//k)
            k+ =1
        
        if k*k ==n:
            yield k
    
    for i in a:
        yield i
