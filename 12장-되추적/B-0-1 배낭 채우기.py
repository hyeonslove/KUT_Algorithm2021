'''
    KOREATECH 2021 Algorithm
'''

from sys import stdin
 
maxProfit = 0
 
 
class Form:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        self.score = self.profit / self.weight
 
    def __str__(self):
        return self.profit + ' ' + self.weight + ' ' + self.score
 
 
def promising(items, W, currProfit, currWeight, index):
    global maxProfit
    if currWeight >= W:
        return False
    nextIndex = index + 1
    bound = currProfit
    totalWeight = currWeight
    while nextIndex < n and totalWeight + items[nextIndex].weight < W:
        totalWeight += items[nextIndex].weight
        bound += items[nextIndex].profit
        nextIndex += 1
    if nextIndex < n:
        bound += (W - totalWeight) * items[nextIndex].score
 
    return bound > maxProfit
 
 
def knapsack(items, include, W, currProfit, currWeight, index):
    global maxProfit
    try:
        if currWeight <= W and currProfit > maxProfit:
            maxProfit = currProfit
 
        if promising(items, W, currProfit, currWeight, index):
            include[index + 1] = True
            knapsack(items, include, W, currProfit + items[index + 1].profit, currWeight + items[index + 1].weight, index + 1)
            include[index + 1] = False
            knapsack(items, include, W, currProfit, currWeight, index + 1)
        print(end='')
    except Exception:
        pass
 
 
testcase = int(stdin.readline().strip())
while testcase:
    bag, n = list(map(int, stdin.readline().strip().split()))
    temp = list(map(int, stdin.readline().strip().split()))
    arr = []
    for i in range(0, len(temp), 2):
        arr.append(Form(temp[i], temp[i + 1]))
    arr.sort(key=lambda x: x.score, reverse=True)
    maxProfit = 0
    knapsack(arr, [False for i in range(len(arr))], bag, 0, 0, -1)
    print(maxProfit)
    testcase -= 1