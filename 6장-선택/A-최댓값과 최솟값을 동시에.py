'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1196
'''

from sys import stdin

INF = 10 ** 9

testcase = int(stdin.readline().strip())

while testcase:
    lenght = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))
    result = [-INF, INF]  # MAX, MIN
    for i in arr:
        if result[0] < i:
            result[0] = i
        elif result[1] > i:
            result[1] = i
    print(' '.join(str(i) for i in result))
    testcase -= 1