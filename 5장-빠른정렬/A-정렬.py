'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1192
'''

from sys import stdin


def quick_sort(arr):
    import random
    if len(arr) <= 1:
        return arr

    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [i for i in arr if i < pivot]
    mid = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return quick_sort(left) + mid + quick_sort(right)


testcase = int(stdin.readline().strip())

while testcase:
    lenght = int(stdin.readline().strip())
    sort_list = quick_sort(list(map(int, stdin.readline().strip().split())))
    print(' '.join([str(i) for i in sort_list]))
    testcase -= 1
