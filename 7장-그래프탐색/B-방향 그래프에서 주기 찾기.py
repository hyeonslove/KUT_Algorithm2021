'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1200
'''

from sys import stdin

testcase = int(stdin.readline().strip())


def DFS(pos, node_data, visited):
    if visited[pos]:
        return True
    visited[pos] = True
    if pos not in node_data:
        return None
    for next_pos in node_data[pos]:
        var = DFS(next_pos, node_data, visited)
        visited[next_pos] = False
        if var is True:
            return var


while testcase:
    node_cnt, graph_cnt = list(map(int, stdin.readline().strip().split()))
    node_info = list(map(int, stdin.readline().strip().split()))
    node_data = dict()

    for i in range(0, graph_cnt * 2, 2):
        if node_info[i] not in node_data:
            node_data[node_info[i]] = dict()
        node_data[node_info[i]][node_info[i + 1]] = None

    for i in range(node_cnt):
        if DFS(i, node_data, [False for _ in range(node_cnt)]) is True:
            print('true')
            break
    else:
        print('false')

    testcase -= 1