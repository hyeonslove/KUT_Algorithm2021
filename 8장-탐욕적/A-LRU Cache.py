'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1202
'''

from sys import stdin
from collections import OrderedDict

testcase = int(stdin.readline().strip())

while testcase:
    cache_cnt, command_cnt = list(map(int, stdin.readline().strip().split()))
    command_list = list(map(int, stdin.readline().strip().split()))
    LRU_cache = OrderedDict()
    result = []
    idx = 0
    while idx < len(command_list):
        opcode = command_list[idx]
        idx += 1
        if opcode == 0:  # put
            key, value = command_list[idx], command_list[idx + 1]

            if LRU_cache.get(key, False):  # exists
                LRU_cache.move_to_end(key, last=True)  # 사용한 것은 맨뒤로
            elif len(LRU_cache) == cache_cnt:
                LRU_cache.popitem(last=False)  # FIFO

            LRU_cache[key] = value
            idx += 2
        else:  # get
            key = command_list[idx]
            value = LRU_cache.get(key, -1)
            if value != -1:
                LRU_cache.move_to_end(key, last=True)  # 쓰여진 것은 맨 뒤로
            result.append(value)
            idx += 1
    print(' '.join(str(i) for i in result))

    testcase -= 1
