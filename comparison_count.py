#Sorts an array by comparison counting
#Input: Array A[0..n − 1] of orderable values
#Output: Array S[0..n − 1] of A’s elements sorted
#in nondecreasing order
#Isiana Carr-Coleman
#Portfolio 1
#CS320
#W22

import time
import random

def comparison_count_sort(lst):
    
    #initializes the count and the sorted list
    count = [0]* len(lst)
    S = [None] * len(lst)

    #traverses through the list and compares values. Adds 1 to the list if it is greater.
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] < lst[j]:
                count[j] = count[j]+1
            else:
                count[i] = count[i]+1
    #Sorts the list based on count in a new list           
    for s in range(0, len(S)):
        S[count[s]] = lst[s]



def main():
    print("This is a program that sorts and unsorted list")
    size = int(input("Enter the list size: ", ))
    trials = int(input("Enter the number of trails: "))

    times = []
                     
    lst1 = []
    for i in range(size):
            lst1.append(random.randrange(10))

    print("Here is your unsorted list: ")
    print(lst1)

    for i in range(trials):
        start = time.time()

        comparison_count_sort(lst1)

        end = time.time()

        elapsed_time = round(end-start, 3)

        times.append(elapsed_time)

        print(elapsed_time)

        print("Here is your sorted list")
        print(lst1)

    print("The average time is: ", sum(times)/trials)
    
if __name__ == "__main__":
    main()
