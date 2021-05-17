'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1204
    DisjointSet
'''

from sys import stdin


class DisjointSet():
    def __init__(self, size):
        self.csize = size
        self.parent = [i for i in range(size)]
        self.size = [1 for _ in range(size)]

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    # min, max
    def union(self, p1, p2):
        parent1 = self.find(p1)
        parent2 = self.find(p2)
        if parent1 == parent2:
            return False
        if parent1 > parent2:
            parent1, parent2 = parent2, parent1

        self.parent[parent2] = self.parent[parent1]
        self.size[parent1] += self.size[parent2]
        self.size[parent2] = 0
        if self.size[parent1] >= self.csize:
            return None
        return True


# params = [int(i) for i in sys.argv[1:]]  # debug
testcase = int(stdin.readline().strip())  # input
# testcase = params[0]  # debug
while testcase:
    node_cnt, edge_cnt = list(map(int, stdin.readline().strip().split()))  # input
    temp = list(map(int, stdin.readline().strip().split()))  # input
    # node_cnt, edge_cnt = params[1], params[2]  # debug
    # temp = params[3:]  # debug
    info = []
    for i in range(0, edge_cnt * 3, 3):
        info.append((temp[i], temp[i + 1], temp[i + 2]))
    diset = DisjointSet(node_cnt)
    info.sort(key=lambda x: x[2])
    result = 0
    for s, e, c in info:
        var = diset.union(s, e)
        if var is True:
            result += c
        elif var is None:
            result += c
            break
    print(result)
    testcase -= 1
