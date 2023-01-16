# import sys
# sys.setrecursionlimit(10**6)
# N, M = map(int, input().split())

# def forward(num,line):
#     if num == 0:
#         line1 = []
#         a = forward(num+1, line1)
#
#         line.append(num)
#         line.extend(line1)
#         return a + 1
#     if num < M:
#         line1 = []
#         line2 = []
#         line3 = []
#
#         line_num = []
#
#         line_num.append(forward(num*2, line1))
#         line_num.append(forward(num+1, line2))
#
#         if num > 2:
#             line3.append(num - 1)
#             line_num.append(forward((num - 1)*2, line3) + 1)
#
#         line.append(num)
#
#         if min(line_num) == line_num[0]:
#             line.extend(line1)
#             return line_num[0] + 1
#         elif min(line_num) == line_num[1]:
#             line.extend(line2)
#             return line_num[1] + 1
#         else:
#             line.extend(line3)
#             return line_num[2] + 1
#
#     elif num == M:
#         line.append(num)
#         return 0
#     else:
#         line3 = []
#         l3 = forward(num-1, line3)
#         line.append(num)
#         line.extend(line3)
#         return l3 + 1
#
# data = []
# length = forward(N, data)
#
# print(length)
# print(*data)


from collections import deque

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0]*100001
move = [0]*100001
bfs()