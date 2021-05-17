'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1191
'''

import collections
from sys import stdin

testcase = int(stdin.readline().strip())

while testcase:
    arr = [int(i) for i in stdin.readline().strip().split(' ')][1:]
    result = dict(collections.Counter(arr))
    print(max(result, key=result.get))
    testcase -= 1