import sys

num = int(sys.stdin.readline())

problem = []

for i in range(0, num):
    data = []
    data.append(int(sys.stdin.readline()))
    data.append(int(sys.stdin.readline()))
    problem.append(data)


for i in problem:
    dp = [list(x for x in range(1, i[1]+1))]
    for n in range(0, i[0]):
        dp_next = []
        for k in range(0, i[1]):
            dp_next.append(sum(dp[-1][0:k + 1]))
        dp.append(dp_next)
    print(dp[i[0]][i[1]-1])