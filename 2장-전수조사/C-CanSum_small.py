'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1187
'''

from sys import stdin


def search_all(arr, origin, target):
    result = sum(arr)
    if result < target:
        for pick in origin:
            arr.append(pick)
            if search_all(arr, origin, target):
                return True
            arr.pop()
    elif result == target:
        return True


testcase = int(stdin.readline().strip())

while testcase:
    target, length = list(map(int, stdin.readline().strip().split()))
    arr = list(map(int, stdin.readline().strip().split()))
    arr.sort()
    ## 최소한 a + b형태가 되어야하므로 최소 2개부터 시작.
    for i in range(length):  # i는 만들 자리수를 뜻함.
        if search_all([], arr, target):
            print('true')
            break
    else:
        print('false')
    testcase -= 1