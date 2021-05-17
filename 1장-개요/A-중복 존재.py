'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1077
'''

from sys import stdin

testcase = int(stdin.readline().strip())

while testcase:
    data_lenght = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(' ')))
    data = set()
    for item in arr:
        data.add(item)
    print('true' if len(data) != data_lenght else 'false')
    testcase -= 1
