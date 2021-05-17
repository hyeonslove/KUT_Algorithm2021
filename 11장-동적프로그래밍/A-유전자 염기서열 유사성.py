'''
    KOREATECH 2021 Algorithm
'''

from sys import stdin

INF = int(1e9)

testcase = int(stdin.readline().strip())

while testcase:
    var = list(map(str, stdin.readline().strip().split()))
    gap_penalty, mismatch_penalty = int(var[0]), int(var[1])
    word1, word2 = var[2], var[3]
    dp = [[INF for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
    dp[0][0] = 0
    for i in range(1, len(word1) + 1):
        dp[i][0] = i * gap_penalty

    for i in range(1, len(word2) + 1):
        dp[0][i] = i * gap_penalty

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else mismatch_penalty),
                           dp[i - 1][j] + gap_penalty,
                           dp[i][j - 1] + gap_penalty)
    print(dp[len(word1)][len(word2)])
    testcase -= 1
