'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1193
'''

from sys import stdin


# merge sort
def merge(left, right):
    result = 0
    v = list()
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            v.append(left[i])
            i += 1
        else:
            v.append(right[j])
            result += len(left) - i  # 정렬 전 오른쪽 만큼 존재하면 더해줌
            j += 1
    if i == len(left):
        v = v + right[j:len(right)]
    if j == len(right):
        v = v + left[i:len(left)]
    return v, result


def merge_sort(v):
    if len(v) <= 1: return v, 0
    m = len(v) // 2
    left, l_cnt = merge_sort(v[0:m])  # 왼쪽 개수
    right, r_cnt = merge_sort(v[m:len(v)])  # 오른쪽 개수
    all, a_cnt = merge(left, right)  # 합친것의 개수
    return all, l_cnt + r_cnt + a_cnt


testcase = int(stdin.readline().strip())
while testcase:
    length = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(' ')))
    _, cnt = merge_sort(arr)
    print(cnt)
    testcase -= 1
