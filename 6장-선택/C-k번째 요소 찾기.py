'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1198
'''

import random
from sys import stdin

INF = -22000000000
testcase = int(stdin.readline().strip())


def RSelect(arr, left, right, target):
    arr = arr[left:right]
    if left == right:
        return arr[left]
    rand_idx = random.randint(0, len(arr) - 1)
    pivot = arr[rand_idx]
    t_left = [i for i in arr if i < pivot]
    t_mid = [i for i in arr if i == pivot]
    t_right = [i for i in arr if i > pivot]

    arr = t_left + t_mid + t_right

    mid_idx = len(t_left) + 1
    if mid_idx == target:
        return pivot
    elif mid_idx < target:
        return RSelect(arr, len(t_left) + len(t_mid), len(arr), target - mid_idx)  # 오른쪽
    elif mid_idx > target:
        return RSelect(arr, 0, mid_idx - 1, target)  # 왼쪽


while testcase:
    lenght, target = list(map(int, stdin.readline().strip().split()))
    arr = list(map(int, stdin.readline().strip().split()))

    print(RSelect(arr, 0, len(arr), target))
    testcase -= 1
