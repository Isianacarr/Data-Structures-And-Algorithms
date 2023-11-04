#this is a program that returns a list of all subsets of a list

import random

def subsets_bu(items):
    '''all substest of items
    	     pre: items is a list
    	     post: returns a list of all the "subsets" of items.'''

    subsets = [[]]

    for i in items:
        subsets += [lst + [i] for lst in subsets]

    return subsets

def subsets_td(items):
    '''all substest of items
        	     pre: items is a list
        	     post: returns a list of all the "subsets" of items.'''

    subsets = [[]]
    size = len(items)

    if size == 0:
       return subsets

    else:
        sets = subsets_td(items[1:])
        return (sets + [[items[0]] + i for i in sets])


def main():

    print("This is a program that displays all the subsets of a list")
    size = int(input("How big is your list:" ))

    lst1 = []
    for i in range(size):
        lst1.append(random.randrange(100))

    subsets = subsets_bu(lst1)
    subsets2 = subsets_td(lst1)

    print("Your list is:")
    print(lst1)

    print("The bottom up approach gave us:")
    print(subsets)
    print()
    print("The top up approach gave us:")
    print(subsets2)



main()


