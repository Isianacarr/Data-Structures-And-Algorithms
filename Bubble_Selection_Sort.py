#Sorts a given array by bubble sort
#Input: An array A[0..n − 1] of orderable elements
#Output: Array A[0..n − 1] sorted in nondecreasing order

import random

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j+1] < lst[j]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def main():
    lst = []
    print("This is a program that sorts and unsorted list")
    size = int(input("Enter the size of the list: ", ))
    
    for i in range(size):
                lst.append(random.randrange(10))

    print("Here is your unsorted list: ")
    print(lst)

    bubble_sort(lst)

    print("Here is your sorted list")
    print(lst)


if __name__ == "__main__":
    main()
