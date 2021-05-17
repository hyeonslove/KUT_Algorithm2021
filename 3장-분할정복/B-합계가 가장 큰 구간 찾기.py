'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1194
'''

from sys import stdin

MIN = -18 ** 5 - 1


def merge(left, right):
    left.reverse()
    temp = 0
    left_part = MIN
    for i in left:
        temp += i
        left_part = max(left_part, temp)

    temp = 0
    right_part = MIN
    for i in right:
        temp += i
        right_part = max(right_part, temp)

    return left_part + right_part


def divide(arr):
    if len(arr) <= 1:
        return arr, arr[0]

    mid = len(arr) // 2
    left, l_val = divide(arr[:mid])  # 왼쪽의 개수
    right, r_val = divide(arr[mid:])  # 오른쪽 개수
    return left + right, max(merge(left, right), l_val, r_val)  #합친것의 개수


testcase = int(stdin.readline().strip())
while testcase:
    length = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))
    print(divide(arr)[1])
    testcase -= 1
