import random

def insertion_sort(lists):

    lst = lists.copy()
    for i in range(len(lst)):
        v = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > v:
            lst[j+1] = lst[j]
            j = j-1
        lst[j + 1] = v

    return lst

def main():

    size = 10
    lst1 = []
    for i in range(size):
        lst1.append(random.randrange(10000))

    sorted = insertion_sort(lst1)

    print(lst1)
    print(sorted)

main()

