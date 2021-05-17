'''
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1203
'''

from sys import stdin

testcase = int(stdin.readline().strip())


class Form:
    def __init__(self, index, deadline, profit):
        self.index = index
        self.deadline = deadline
        self.profit = profit

    def __str__(self):
        return str(self.index) + ' ' + str(self.deadline) + ' ' + str(self.profit)


while testcase:
    length = int(stdin.readline().strip())
    temp = list(map(int, stdin.readline().strip().split()))
    # jobs = (index, deadline, profit)
    jobs = [Form(i // 2 + 1, temp[i], temp[i + 1]) for i in range(0, len(temp), 2)]
    jobs.sort(key=lambda x: x.profit, reverse=True)
    maxD = max(jobs, key=lambda x: x.deadline).deadline
    scheduled = list(None for i in range(maxD + 1))
    scheduled[jobs[0].deadline] = jobs[0]

    i = 1
    while i < len(jobs):
        j = jobs[i].deadline
        while j > 0:
            if scheduled[j] is None:
                scheduled[j] = jobs[i]
                break
            j -= 1
        i += 1
    result = [i.index for i in scheduled if i is not None]
    result.sort()
    print(' '.join(str(i) for i in result))
    testcase -= 1