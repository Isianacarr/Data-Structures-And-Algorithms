from math import *

#function that finds the squareroot of a number
def sqrtt(n):
    for i in range(1, n+1):
        if i * i > n:
            return i - 1
            
#function that finds the common elements between two lists
def findcommon(lst1, lst2):
    lst3 = []

    while len(lst2) > 0:
        for p in lst1:
            if p in lst2:
                lst3.append(p)
                lst2.remove(p)
        return lst3
    print(lst3)



