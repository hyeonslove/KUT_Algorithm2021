'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1192

    분할정복을 이용한 합병정렬렬
'''

from sys import stdin


# merge sort
def merge(left, right):
    v = list()
    i = 0
    j = 0
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            v.append(left[i])
            i += 1
        else:
            v.append(right[j])
            j += 1
    if i == len(left): v = v + right[j:len(right)]
    if j == len(right): v = v + left[i:len(left)]
    return v


def merge_sort(v):
    if len(v) <= 1: return v
    m = len(v) // 2
    left = merge_sort(v[0:m])  # 왼쪽 정렬
    right = merge_sort(v[m:len(v)])  # 오른쪽 정렬
    return merge(left, right)


testcase = int(stdin.readline().strip())

while testcase:
    length = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(' ')))
    print(' '.join(str(i) for i in merge_sort(arr)))
    testcase -= 1
