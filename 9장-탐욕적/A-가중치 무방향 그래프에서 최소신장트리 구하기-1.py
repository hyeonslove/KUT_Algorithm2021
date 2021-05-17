'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1204
    Prim
'''

import heapq
import sys
from sys import stdin


def prim(start, graph):
    result = 0
    # 방문 확인을 위한 변수
    visited = [False for _ in range(len(graph))]
    task = []
    # 첫 시작점에서 갈 수 있는 범위를 등록
    for end, cost in enumerate(graph[start]):
        if cost != 0:
            heapq.heappush(task, (cost, (start, end)))

    # heap이 빌 때까지 반복
    while len(task):
        # 가장 작은 비용의 s -> e를 가져옴
        cost, (s, e) = heapq.heappop(task)

        # 둘중에 한곳이라도 방문이 안되어있으면
        if visited[s] == False or visited[e] == False:
            # 방문처리를 해주고
            visited[s] = visited[e] = True
            # 코스트를 증가
            result += cost

            # 다른 방문점을 추가시킨다.
            for end, cost in enumerate(graph[e]):
                if cost != 0:  # 코스트가 0이 아니면서
                    if not visited[end]:  # 방문한 지점이 아니면
                        heapq.heappush(task, (cost, (e, end)))  # 추가
    return result


# params = [int(i) for i in sys.argv[1:]]  # debug
testcase = int(stdin.readline().strip())  # input
# testcase = params[0]
while testcase:
    node_cnt, edge_cnt = list(map(int, stdin.readline().strip().split()))  # input
    temp = list(map(int, stdin.readline().strip().split()))  # input
    # node_cnt, edge_cnt = params[1], params[2]  # debug
    # temp = params[3:]  # debug
    graph = [[0 for _ in range(node_cnt)] for _ in range(node_cnt)]
    for i in range(0, edge_cnt * 3, 3):
        graph[temp[i]][temp[i + 1]] = temp[i + 2]
        graph[temp[i + 1]][temp[i]] = temp[i + 2]

    print(prim(0, graph))
    testcase -= 1
