import random


def merge_sort(lst):



    if len(lst) > 1:
        mid = len(lst) // 2
        lst1 = lst[:mid]
        lst2 = lst[mid:]
        merge_sort(lst1)
        merge_sort(lst2)

        return merge(lst1, lst2, lst)




def merge(lst1, lst2, lst):

    i = 0
    j = 0
    k = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            lst[k] = lst1[i]
            i += 1

        else:
            lst[k] = lst2[j]
            j += 1
        k += 1

    if i == len(lst1):
        for u in range(j, len(lst2)):
            lst[k] = lst2[u]
            k += 1
    else:
        for u in range(i, len(lst1)):
            lst[k] = lst1[u]
            k += 1



    return lst


def main():

    size = 10
    lst1 = []
    for i in range(size):
        lst1.append(random.randrange(100))



    print(lst1)
    print(merge_sort(lst1))

main()





