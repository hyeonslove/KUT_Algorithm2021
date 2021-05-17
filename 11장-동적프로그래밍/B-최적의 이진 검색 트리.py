'''
    KOREATECH 2021 Algorithm
'''

from sys import stdin

testcase = int(stdin.readline().strip())
while testcase:
    cnt = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))
    dp = [[0 for _ in range(cnt + 2)] for _ in range(cnt + 2)]

    for s in range(cnt):
        for i in range(1, cnt - s + 1):
            if s == 0:
                dp[i][i + s] = arr[i - 1]
            else:
                resum = 0
                for k in range(i, i + s + 1):
                    resum += dp[k][k]
                dp[i][i + s] = resum + min([dp[i][r - 1] + dp[r + 1][i + s] for r in range(i, i + s + 1)])
    print(dp[1][cnt])
    testcase -= 1
