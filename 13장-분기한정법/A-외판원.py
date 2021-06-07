'''
    KOREATECH 2021 Algorithm
'''

import heapq
import copy
from sys import stdin

INF = int(1e9)


class Node:
    def __init__(self, level, bound, tour):
        self.level = level
        self.bound = bound
        self.tour = tour

    def __lt__(self, other):
        return self.bound < other.bound


def getBound(tours):
    bound = 0
    calc_bound = []
    for i in range(len(tours) - 1):
        bound += arr[tours[i]][tours[i + 1]]
        calc_bound.append(tours[i])
    bound += min([val for idx, val in enumerate(arr[tours[-1]]) if idx not in tours[:-1]])
    calc_bound.append(tours[-1])
    for i in range(1, n):
        if i not in calc_bound:
            bound += min([val for idx, val in enumerate(arr[i]) if idx not in tours[1:]])
    return bound


def getLength(tours):
    length = 0
    for i in range(len(tours) - 1):
        length += arr[tours[i]][tours[i + 1]]
    return length


testcase = int(stdin.readline().strip())

while testcase:
    n = int(stdin.readline().strip())
    arr = [[INF if int(item) == 0 else int(item) for item in stdin.readline().strip().split(' ')] for _ in range(n)]
    arr = [[INF if item == -1 else item for item in items] for items in arr]

    min_value = sum([min([item for item in items]) for items in arr])
    min_length = INF
    que = []
    heapq.heappush(que, Node(0, min_value, [0]))
    while len(que):
        node = heapq.heappop(que)
        if node.bound < min_length:
            for i in range(1, n):
                if i in node.tour:
                    continue
                if arr[node.tour[node.level]][i] == INF:
                    continue
                next_tour = copy.deepcopy(node)
                next_tour.level = node.level + 1
                next_tour.tour.append(i)

                if next_tour.level == n - 1:
                    next_tour.tour.append(0)
                    length = getLength(next_tour.tour)
                    min_length = length if min_length > length else min_length
                else:
                    next_tour.bound = getBound(next_tour.tour)
                    if (next_tour.bound < min_length):
                        heapq.heappush(que, next_tour)
    print(min_length)
    testcase -= 1
