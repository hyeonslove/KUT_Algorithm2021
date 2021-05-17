'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1185
'''

from sys import stdin


def search_all(start, remain):
    if not remain:
        return 1

    result = 0
    for i in range(start, n):
        if not visit[i]:
            for j in range(i + 1, n):
                if not visit[j] and are_Friend[i][j]:
                    visit[i] = visit[j] = True  # 방문 등록
                    result += search_all(i, remain - 2)  # 짝을 찾았으니 남은 수는 remain - 2, 다음 짝을 탐색
                    visit[i] = visit[j] = False  # 방문 등록 해제
    return result


testcase = int(stdin.readline().strip())

while testcase:
    n, m = map(int, input().split())
    visit = [False] * n
    are_Friend = [[False] * n for _ in range(n)]
    friends_info = list(map(int, stdin.readline().strip().split()))

    ## 친구 정보를 입력해줌
    for i in range(0, len(friends_info), 2):
        are_Friend[friends_info[i]][friends_info[i + 1]] = True
        are_Friend[friends_info[i + 1]][friends_info[i]] = True

    print(search_all(0, n))
    testcase -= 1
