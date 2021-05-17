'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1201
'''

from queue import PriorityQueue
from sys import stdin

INF = int(10e9)
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
    node_all_info = list(map(int, stdin.readline().strip().split()))

    node_cnt, edge_cnt, start_node, end_node_cnt = \
        node_all_info[0], node_all_info[1], node_all_info[2], node_all_info[3]
    end_node = [node_all_info[i] for i in range(4, len(node_all_info))]

    node_edge_info = list(map(int, stdin.readline().strip().split()))
    node_data = dict()
    distance = [INF] * (node_cnt + 1)
    for i in range(0, edge_cnt * 3, 3):
        if node_edge_info[i] not in node_data:
            node_data[node_edge_info[i]] = dict()
        node_data[node_edge_info[i]][node_edge_info[i + 1]] = node_edge_info[i + 2]

    que = PriorityQueue()
    que.put((0, start_node))
    while que.qsize():
        dist, pos = que.get()
        if distance[pos] < dist:
            continue
        if pos in node_data:
            for i in node_data[pos]:
                cost = dist + node_data[pos][i]

                if cost < distance[i]:
                    distance[i] = cost
                    que.put((cost, i))
    result = []
    for i in end_node:
        result.append(str(distance[i] if distance[i] != INF else -1))
    print(' '.join(result))
    testcase -= 1
