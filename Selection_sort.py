#Sorts a given array by selection sort
#Input: An array A[0..n − 1] of orderable elements
#Output: Array A[0..n − 1] sorted in nondecreasing order

import random

def selection_sort(lst1):

    for i in range(len(lst1)-1):
        minn = i
        for j in range(i+1, len(lst1)):
            if lst1[j] < lst1[minn]:
                minn = j
            lst1[i], lst1[minn] = lst1[minn], lst1[i]
    print(lst1)

def main():
    lst1 = []
    print("This is a program that sorts and unsorted list")
    size = int(input("Enter the size of the list: " ))
    
    for i in range(size):
                lst1.append(random.randrange(10))
    print("Here is your unsorted list: ")
    print(lst1)
    selection_sort(lst1)

    print("Here is your sorted list")
    print(lst1)

    

if __name__ == "__main__":
    main()

                
                
