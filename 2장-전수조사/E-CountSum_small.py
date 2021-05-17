'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1189
'''

from sys import stdin


def search_all(arr, origin, target):
    result = 0
    total = sum(arr)
    if total < target:
        for pick in origin:
            arr.append(pick)
            result += search_all(arr, origin, target)
            arr.pop()
    elif total == target:
        return 1
    return result


testcase = int(stdin.readline().strip())

while testcase:
    target, length = list(map(int, stdin.readline().strip().split()))
    arr = list(map(int, stdin.readline().strip().split()))
    arr.sort()
    result = 0

    result += search_all([], arr, target)

    print(result)
    testcase -= 1
