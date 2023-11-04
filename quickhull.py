# quickhull.py
# This program implements the quickhull algorithm and graphs it.
'''Input: a list of points.
Output: a list of segments (pairs of points), that describe the convex hull'''

from collections import namedtuple
import matplotlib.pyplot as plt
import numpy as np
from random import randrange

Point = namedtuple("Point", "x , y")


def quickhull(points):
    '''s1 {p when p is left of p1pn} , s2 {p when p is right of p1pn}
'''
    lst_size = len(points)
    if lst_size > 2:
        p_first = min(points)
        p_last = max(points)
        s1 = [p for p in points if (calc_determ(p_first, p_last, p)) > 0]
        s2 = [p for p in points if calc_determ(p_first, p_last, p) < 0]
        determinants_s1 = {p: calc_determ(p_first, p_last, p) for p in s1}
        determinants_s2 = {p: calc_determ(p_first, p_last, p) for p in s2}

        hull1 = halfhull(p_first, p_last, s1, determinants_s1)
        hull2 = halfhull(p_last, p_first, s2, determinants_s2)
        convex_hull = hull1 + hull2
        return convex_hull

    else:
        return points


def halfhull(p1, pn, s, determinants):
    s_size = len(s)
    half1 = []
    if s_size == 0:
        return [(p1, pn)]
    if s_size >= 1:
        pmax_determinants_so_far = 0
        pmax = p1

        for p in s:
            determ = abs(calc_determ(p1, pn, p))
            if determ > pmax_determinants_so_far:
                pmax_determinants_so_far = determ
                pmax = p

        s1 = [p for p in s if calc_determ(p1, pmax, p) > 0]
        s2 = [p for p in s if calc_determ(pmax, pn, p) > 0]

        determinant_lst1 = {p: calc_determ(p1, pmax, p) for p in s1}
        determinant_lst2 = {p: calc_determ(pmax, pn, p) for p in s2}

        half1 = halfhull(p1, pmax, s1, determinant_lst1)
        half2 = halfhull(pmax, pn, s2, determinant_lst2)

        return half1 + half2


def calc_determ(p1, p2, p3):
    arrray = np.array([[p1.x, p1.y, 1], [p2.x, p2.y, 1], [p3.x, p3.y, 1]])
    det = np.linalg.det(arrray)
    return det


def display(points):
    # all points
    x = [p.x for p in points]
    y = [p.y for p in points]
    plt.plot(x, y, marker='D', linestyle='None')

    '''# hull points
    hx = [p.x for p in hull]
    hy = [p.y for p in hull]
    plt.plot(hx, hy)'''

    plt.title('Convex Hull')
    plt.show()


def main():
    print("This is a program that find a convex hull given a set of points")
    n = int(input("How many points would you like to include? :"))

    points = [Point(randrange(1, 800), randrange(1, 800)) for i in range(n)]

    hull = quickhull(points)
    print("Points on hull:", quickhull(points))
    display(points)


if __name__ == '__main__':
    main()
