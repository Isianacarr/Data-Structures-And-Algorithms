import random
import functools
memoize = functools.lru_cache(maxsize=None)
import sys
sys.setrecursionlimit(10000000)

class KnapSack:

    def __init__(self, items):
        self.items = list(items)
        self.F = memoize(self.F)

    def F(self, n, C):
        if n == -1 or C == -1:
            return 0
        else:
            wn, vn = self.items[n]

            if C - wn < 0:
                return self.F(n - 1, C)
            else:
                return max(self.F(n - 1, C), vn + self.F(n - 1, C - wn))

    def solution(self, n, C):
        result = self.F(n, C)
        values = []

        while n >= 0:
            if self.F(n, C) > self.F(n - 1, C):
                w, v = self.items[n]
                values.append(v)
                C -= w
            n -= 1

        return values, result

def main():
    print("This program uses dynamic programming to solve the Knapsack Problem.")
    print("ks = Knapsack([(4, 8), (1, 15), (4, 5), (1, 20), (30, 4)])")
    ks = KnapSack([(4, 8), (1, 15), (4, 5), (1, 20), (30, 4)])
    print("ks.solution(4, 10)")
    print("Solution to Knapsack Problem is: ", ks.solution(4, 10))


if __name__ == "__main__":
    main()