#project-1: write a python program that outputs all possible strings formed by using list of characters e.g. ['c','a','t'] exactly once/

from math import factorial
from random import shuffle

def strin_gen(li):
    ls=[]
    s=factorial(len(li))
    while len(ls)<s:
        strin=''.join(li)
        if (strin in ls)==False:
            ls.append(strin)
        shuffle(li)
    
    return ls