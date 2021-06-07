'''
    KOREATECH 2021 Algorithm
'''

from sys import stdin
import heapq
 
maxProfit = 0
 
 
class Form:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        self.score = self.profit / self.weight
 
    def __str__(self):
        return self.profit + ' ' + self.weight + ' ' + self.score
 
 
class Node:
    def __init__(self, level, currProfit, currWeight, bound):
        self.level = level
        self.currProfit = currProfit
        self.currWeight = currWeight
        self.bound = bound
 
    def __lt__(self, other):
        return self.bound > other.bound
 
 
def get_bound(items, W, currProfit, currWeight, index):
    if currWeight>=W: return 0
    nextIndex = index+1
    bound = currProfit
    totalWeight = currWeight
    while nextIndex < n and totalWeight + items[nextIndex].weight < W:
        totalWeight += items[nextIndex].weight
        bound += items[nextIndex].profit
        nextIndex += 1
    if nextIndex < n:
        bound += (W - totalWeight) * items[nextIndex].score
 
    return bound
 
 
testcase = int(stdin.readline().strip())
while testcase:
    bag, n = list(map(int, stdin.readline().strip().split()))
    temp = list(map(int, stdin.readline().strip().split()))
    arr = []
    for i in range(0, len(temp), 2):
        arr.append(Form(temp[i], temp[i + 1]))
    arr.sort(key=lambda x: x.score, reverse=True)
    maxProfit = 0
    que = []
    bound = get_bound(arr, bag, 0, 0, -1)
    heapq.heappush(que, Node(-1, 0, 0, bound))
    while len(que):
        node = heapq.heappop(que)
        #print(node.level, node.currProfit, node.currWeight, node.bound)
        if node.bound > maxProfit:
            node.level += 1
            if node.level >= len(arr):
                continue
            node.currWeight += arr[node.level].weight
            node.currProfit += arr[node.level].profit
            if node.currWeight <= bag and node.currProfit > maxProfit:
                maxProfit = node.currProfit
 
            node.bound = get_bound(arr, bag, node.currProfit, node.currWeight, node.level)
            if node.bound > maxProfit:
                heapq.heappush(que, Node(node.level, node.currProfit, node.currWeight, node.bound))
            node.currWeight -= arr[node.level].weight
            node.currProfit -= arr[node.level].profit
 
            node.bound = get_bound(arr, bag, node.currProfit, node.currWeight, node.level)
            if node.bound > maxProfit:
                heapq.heappush(que, Node(node.level, node.currProfit, node.currWeight, node.bound))
 
    print(maxProfit)
    testcase -= 1