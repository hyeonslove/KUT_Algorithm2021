'''
    KOREATECH 2021 Algorithm
'''

from sys import stdin

INF = int(1e9)

testcase = int(stdin.readline().strip())

while testcase:
    node_cnt, edge_cnt = list(map(int, stdin.readline().strip().split()))
    temp = list(map(int, stdin.readline().strip().split()))
    d = [[0 if i == j else INF for i in range(node_cnt)] for j in range(node_cnt)]
    for i in range(0, edge_cnt * 3, 3):
        d[temp[i]][temp[i + 1]] = temp[i + 2]

    for k in range(node_cnt):
        for i in range(node_cnt):
            for j in range(node_cnt):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    for i in range(node_cnt):
        if d[i][i] < 0:
            print('-1')
            break
    else:
        result = [None, None, -INF]
        for i in range(node_cnt):
            for j in range(node_cnt):
                if d[i][j] > result[2] and d[i][j] < (int(1e9) - int(1e8)):
                    result = [i, j, d[i][j]]
        print(' '.join(map(str, result)))
    testcase -= 1
