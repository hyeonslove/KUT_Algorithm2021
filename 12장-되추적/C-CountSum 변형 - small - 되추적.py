'''
    KOREATECH 2021 Algorithm
'''

import collections
from sys import stdin
 
 
def promising(nums, currTotal, leftTotal, W, index):
    return currTotal + leftTotal >= W and (currTotal == W or currTotal + nums[index] <= W)
 
 
def DFS(nums, included, currTotal, leftTotal, W, index):
    global result
    if promising(nums, currTotal, leftTotal, W, index):
        if currTotal == W:
            result += 1
        else:
            included[index] = True
            leftTotal -= nums[index]
            DFS(nums, included, currTotal + nums[index], leftTotal, W, index + 1)
            included[index] = False
            DFS(nums, included, currTotal, leftTotal, W, index + 1)
 
 
testcase = int(stdin.readline().strip())
 
while testcase:
    target, length = list(map(int, stdin.readline().strip().split()))
    case = list(map(int, stdin.readline().strip().split()))
    case.sort()
    deq = collections.deque(case)
    result = 0
    DFS(case, [False for i in range(length)], 0, sum(case), target, 0)
    print(result)
    testcase -= 1
