'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1199
'''

from queue import Queue
from sys import stdin

testcase = int(stdin.readline().strip())

while testcase:
    node_cnt, graph_cnt = list(map(int, stdin.readline().strip().split()))
    node_info = list(map(int, stdin.readline().strip().split()))
    node_data = dict()
    ## 인접리스트의 역방향까지 표시해줌
    for i in range(0, graph_cnt * 2, 2):
        if node_info[i] not in node_data:
            node_data[node_info[i]] = dict()
        if node_info[i + 1] not in node_data:
            node_data[node_info[i + 1]] = dict()
        node_data[node_info[i]][node_info[i + 1]] = None
        node_data[node_info[i + 1]][node_info[i]] = None

    ## 방문기록
    visited = [False for i in range(node_cnt)]

    graph_cnt_result = 0  # 그래프의 개수
    graph_deapth_result = 0  # 최대 그래프 깊이 개수
    for i in range(node_cnt):  # 0번부터 node cnt만큼 한번씩 탐색함.
        total = 0
        if not visited[i]:  # 방문하지 않은 지점이라면
            graph_cnt_result += 1  # 그래프가 존재함
            que = Queue()
            que.put(i)
            while que.qsize():
                move = que.get()
                if not visited[move]:
                    total += 1
                    visited[move] = True
                    if move in node_data:
                        for i in node_data[move]:
                            que.put(i)
        if total > graph_deapth_result:
            graph_deapth_result = total
    print(graph_cnt_result, graph_deapth_result)
    testcase -= 1