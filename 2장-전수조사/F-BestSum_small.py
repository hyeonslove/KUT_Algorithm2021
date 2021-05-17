'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1190
'''

from sys import stdin


def search_all(arr, origin, target):
    total = sum(arr)
    if total < target:
        for pick in origin:
            arr.append(pick)
            search_all(arr, origin, target)
            arr.pop()
    elif total == target:
        print_list.append(arr[:])


testcase = int(stdin.readline().strip())
while testcase:
    target, length = list(map(int, stdin.readline().strip().split()))
    arr = list(map(int, stdin.readline().strip().split()))
    print_list = []
    search_all([], arr, target)
    if len(print_list) > 0:
        smallest = min(print_list, key=lambda x: len(x))
        print(len(smallest), ' '.join(str(i) for i in smallest))
    else:
        print(-1)
    testcase -= 1