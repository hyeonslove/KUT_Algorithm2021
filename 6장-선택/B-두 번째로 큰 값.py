'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1196
'''

from sys import stdin

INF = -22000000000
testcase = int(stdin.readline().strip())

while testcase:
    lenght = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))
    result = [INF, INF]  # 1번 진값, 계속 이긴값

    for i in arr:
        if i > result[1]:  # 만약 계속 이긴값보다 크면
            result[0] = result[1]  # 계속 이긴값은 1번 진 값으로 내려오고
            result[1] = i  # 계속 이긴값을 최고로
        else:
            if i > result[0]:  # 만약 계속 이긴값보단 작은데 1번 진값보단 크면
                result[0] = i  # 2번진 값을 대입

    print(result[0])
    testcase -= 1