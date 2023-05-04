import sys

N, M, B = map(int, sys.stdin.readline().split())

data = []

for i in range(0, N):
    in_data = list(map(int, sys.stdin.readline().split()))
    for k in in_data:
        data.append(k)

result = []
data.sort(key=lambda x: -x)

for height in range(0, 257):
    time = 0
    inb = B
    for i in data:
        if i > height:
            time += (i-height)*2
            inb += (i-height)
        elif i < height:
            time += (height - i)
            inb -= (height - i)
            if inb < 0:
                time = 99999999
                break
    result.append([time, height])

result.sort(key=lambda x: (x[0], -x[1]))
print(str(result[0][0]) + " " + str(result[0][1]))

# time = 0
#
# sum = sum(map(sum, data))
# avg = round(sum/(N * M))
# while min(map(min, data)) != max(map(max, data)):
#     stack = []
#     for i in range(0, N):
#         for k in range(0, M):
#             if avg < data[i][k]:
#                 #블럭 삭제 2초, 인벤토리 추가
#                 minus = data[i][k] - avg # 제거 블럭 개수
#                 B += minus # 인벤토리 저장
#                 time += 2*minus # 시간 증가
#                 data[i][k] = avg # 평단화
#             elif avg > data[i][k]:
#                 #블럭 설치 1초, 인벤토리 -1 만약 0이면 stack추가
#                 #다 반복후 인벤토리 여부에 따라 설치 또는 avg - 1 => N * M - len(stack)만큼 인벤토리
#                 plus = avg - data[i][k] # 추가 블럭 개수
#                 if B < plus:
#                     stack.append([i, k, plus]) # 스택 추가
#                 else:
#                     time += plus # 시간 증가
#                     data[i][k] = avg  # 평단화
#     if len(stack) != 0:
#         sum_stack = 0
#         for i in stack:
#             sum_stack += i[2]
#
#         if sum_stack > B:
#             avg -= 1
#         else:
#             for i in stack:
#                 data[i[0]][i[1]] = avg
#                 time += i[2]
#
# print(time, avg)
# # 시간 고려.. 모든 avg 검토