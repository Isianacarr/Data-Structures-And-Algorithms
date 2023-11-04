import random
from comparison_count import *
from Selection_sort import *
from Bubble_Selection_Sort import *
import time


def multisorter(sort, lst):
    #takes in an unsorted list and a sorting tyoe and performs that specific sort on the list
    
    if sort == 1:
        bubble_sort(lst)
    elif sort == 2:
        selection_sort(lst)
    elif sort == 3:
        comparison_count_sort(lst)
    else:
        print("That is not a valid entry")


def main():
    #Asks user to select sort, number of trials and list size
    
    print("This is a program that allows users to determine sorting algorithm efficiency")
    print("To choose Bubble sort enter 1")
    print("To choose Selection sort enter 2")
    print("To choose Count sort enter 3")

    sort = int(input("Please enter your selection: ", ))
    size = int(input("Please enter your list size: ", ))
    trials = int(input("Please enter the number of trials: ", ))

    times = []
    lst1 = []

    #initalizes list based on user input for list size   
    for i in range(size):
        lst1.append(random.randrange(100000))


    #times the amount of time each trial runs and returns an average
    for i in range(trials):
        start = time.time()
        

        multisorter(sort,lst1)
        end = time.time()

        elapsed_time = round(end-start, 3)

        times.append(elapsed_time)

        print(elapsed_time)

    print("The average time is: ", round(sum(times)/len(lst1),5))

main()
        


    
