'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1186
'''

from sys import stdin

# 각 사진의 순서대로 좌표를 입력해준 것
coverType = [[(0, 0), (1, 0), (0, 1)], [(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)], [(0, 0), (1, 0), (1, -1)]]


def set_cover(board, y, x, type, delta):
    ok = True
    # L자 모양은 총 3칸이므로 3번을 반복해야함.
    for idx in range(3):
        ny = y + coverType[type][idx][0]
        nx = x + coverType[type][idx][1]
        # 더해지려는 좌표가 범위를 벗어나면 False
        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            ok = False
        else:
            # 범위는 벗어나지 않으나, 이미 덮힌 칸을 덮을 경우 1보다 크므로 1보다 크면 False
            board[ny][nx] += delta  # 칸을 덮어주는 부분
            if board[ny][nx] > 1:
                ok = False

    return ok


def cover(board):
    y, x = -1, -1
    for ty in range(len(board)):
        for tx in range(len(board[0])):
            # 첫 시작위치를 찾아냄 (순서 강제)
            if board[ty][tx] == 0:
                x = tx
                y = ty
                break
        if y != -1:
            break

    # 만약 모든 칸이 덮힐 경우 1를 반환 함.
    if y == -1:
        return 1
    ret = 0

    # L자 모양으로 덮을 수 있는 경우의 수는 4가지이므로 각각 다 덮어봄.
    for type in range(4):
        if set_cover(board, y, x, type, 1):  # 만약 덮혀진다면
            ret += cover(board)  # 나머지 부분을 덮어줌
        set_cover(board, y, x, type, -1)  # 덮힌 부분을 다시 빼줌

    return ret  # 덮힌 부분을 누적하여 리턴함


testcase = int(stdin.readline().strip())
while testcase:
    y, x = list(map(int, stdin.readline().strip().split(' ')))

    board = [[1 if i == '#' else 0 for i in stdin.readline().strip()] for _ in range(y)]
    print(cover(board))
    testcase -= 1
