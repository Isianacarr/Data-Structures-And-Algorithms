# Priority Queue.py
# This program implements a PriorityQueue class using a Python list managed as a heap

from math import isqrt
from random import randrange


class PriorityQueue:

    def __init__(self, items=[]):
        self.heap = list(items)
        self._build_heap()

    def _largest_child(self, i):
        """ returns index of node i's largest child or None when node i is a leaf """
        try:
            left_child = self.heap[2 * i + 1]
            try:
                right_child = self.heap[2 * i + 2]
                if right_child > left_child:
                    return 2 * i + 2
                else:
                    return 2 * i + 1
            except:
                return 2 * i + 1
        except:
            return None

    def _bubble_up(self, i):
        """ restore heap by bubbling up from node i """
        while i > 0:
            parenti = (i - 1) // 2
            if self.heap[i] <= self.heap[parenti]:
                break
            self.heap[i], self.heap[parenti] = self.heap[parenti], self.heap[i]
            i = parenti

    def _bubble_down(self, i):
        """ restore heap by bubbling down from node i """
        k = self._largest_child(i)
        if k and (self.heap[k] > self.heap[i]):
            self.heap[k], self.heap[i] = self.heap[i], self.heap[k]
            self._bubble_down(k)

    def _build_heap(self):
        size = len(self.heap)
        floor = (size - 1) // 2
        for i in range(floor, -1, -1):
            k = i
            v = self.heap[k]
            heapify = False
            while not heapify and 2 * k + 1 < size:
                j = 2 * k + 1
                if j < (size - 1):  # there are 2 children
                    if self.heap[j] < self.heap[j + 1]:
                        j = j + 1
                if v >= self.heap[j]:
                    heapify = True
                else:
                    self.heap[k] = self.heap[j]
                    k = j
            self.heap[k] = v

    def add(self, item):
        """ add item to the queue """
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def get_max(self):
        """ returns and removes highest priority item """
        assert self.heap

        if len(self.heap) == 1:
            return self.heap.pop()
        item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._bubble_down(0)
        return item

    def get_size(self):
        return len(self.heap)


def heapsort(lst):
    pq = PriorityQueue(lst)
    sorted_heap = []
    for i in range(pq.get_size()):
        sorted_heap.append(pq.get_max())
    return sorted_heap[::-1]


def main():
    print("This program implements a PriorityQueue class using a Python list managed as a heap.")
    n = int(input("Enter the number of nodes in your heap: "))
    random_lst = [randrange(0, 100) for i in range(0, n)]
    print("Initial list: ", random_lst)
    sorted_list = heapsort(random_lst)
    print("Your sorted list is: ", sorted_list)


if __name__ == '__main__':
    main()