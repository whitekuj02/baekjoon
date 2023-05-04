import sys

num = int(sys.stdin.readline())

data = []
data_dp = []
for i in range(0, num):
    row, col, number = map(int, sys.stdin.readline().split())
    dp = [[0 for _ in range(0, row)] for _ in range(0, col)]
    for _ in range(0, number):
        x, y = map(int, sys.stdin.readline().split())
        dp[y][x] = 1
    data.append([row,col,number])
    data_dp.append(dp)

for i in range(0, num):
    
