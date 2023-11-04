#This is an implementation of the Sieve of Eratosthenes
#Input: A positive interger n>1
#Output: Array L of all prime numbers less than or equal to n
#Isiana Carr-Coleman
#Cs 320

from math import *

def sieve(n):
    #Creates a list with all the possible primes up to N
    lst = [0,0]
    for x in range(2,n+1):
        lst.append(x)

    #Enumeration is for debugging purposes and to keep track of position
    #As well as print stmts commented out below
    for count, l in enumerate(lst):
        if l <= floor(sqrt(n)):
            if l !=0:
                j = l * l
                #print(count , l, j)
                while j <= n:
                    if j in lst:
                        lst.remove(j)
                    j = j + l
                    #print(count , l, j, lst)
    return lst

def main():
    print("This is a program that finds the array of primes <= N")
    n = int(input("Please enter n:" ))

    print("The list of primes less than or equal to", n , "are", sieve(n))

main()
            
                    
                    
        
                    
                    
        
            
            
    
