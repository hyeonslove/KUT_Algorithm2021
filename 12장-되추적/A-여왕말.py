'''
    KOREATECH 2021 Algorithm
'''

from sys import stdin
 
 
def promising(cols, row):
    flag = True
    r = 0
    while r < row and flag:
        if (cols[r] == cols[row]) or (abs(cols[r] - cols[row]) == (row - r)):
            flag = False
            break
        r += 1
    return flag
 
 
def DFS(cols, row):
    global result
    for c in range(len(cols)):
        cols[row] = c
        if promising(cols, row):
            if row + 1 == len(cols):
                result.append(cols[:])
            else:
                DFS(cols, row + 1)
 
 
testcase = int(stdin.readline().strip())
 
while testcase:
    data = int(stdin.readline().strip())
    result = []
    DFS([0 for i in range(data)], 0)
    if len(result) == 0:
        print()
    else:
        for items in result:
            for item in items:
                print(''.join(['Q' if idx == item else 'X' for idx in range(len(items))]))
    testcase -= 1
