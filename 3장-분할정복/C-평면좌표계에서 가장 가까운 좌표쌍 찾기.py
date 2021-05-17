'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1195
    Nlog(N)
'''

import math
from sys import stdin


def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def closeSplitPair(px, py, delta):
    delta_t = math.sqrt(delta)
    midx = px[len(px) // 2][0]
    range_arr = []
    for i in py:
        if midx - delta_t < i[0] < midx + delta_t:
            range_arr.append(i)

    for i in range(len(range_arr)):
        for j in range(i + 1, i + 8):
            try:
                dist = distance(range_arr[i], range_arr[j])
                if dist < delta:
                    delta = dist
            except IndexError:
                break
    return delta


def closestPair(px, py):
    if len(px) == 2:
        return distance(px[0], px[1])
    if len(px) <= 3:
        return min(distance(px[0], px[1]), distance(px[1], px[2]), distance(px[2], px[0]))

    sort_dict_xL = dict()
    pxL = px[:len(px) // 2]
    pyL = []
    for i in py:
        sort_dict_xL[i] = 0

    for i in pxL:
        sort_dict_xL[i] += 1
    for i in sort_dict_xL:
        if sort_dict_xL[i] > 0:
            pyL.append(i)

    sort_dict_xR = dict()
    pxR = px[len(px) // 2:]
    pyR = []
    for i in py:
        sort_dict_xR[i] = 0

    for i in pxR:
        sort_dict_xR[i] += 1
    for i in sort_dict_xR:
        if sort_dict_xR[i] > 0:
            pyR.append(i)

    delta = min(closestPair(pxL, pyL), closestPair(pxR, pyR))
    return closeSplitPair(px, py, delta)


testcase = int(stdin.readline().strip())

while testcase:
    length = int(stdin.readline().strip())
    temp_data = list(map(int, stdin.readline().strip().split()))
    pos_arr = [(temp_data[i], temp_data[i + 1]) for i in range(0, length * 2, 2)]

    px = pos_arr[:]
    py = pos_arr[:]
    px.sort(key=lambda x: x[0])
    py.sort(key=lambda x: x[1])

    result = closestPair(px, py)
    print('%.2f' % math.sqrt(result))
    testcase -= 1
