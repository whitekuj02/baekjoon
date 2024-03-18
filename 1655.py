# import sys
# from collections import deque

# def binary_search(queue, data, start, end): # 넣어야 하는 위치를 알려주는 함수
    
#     if start - end == 1: # 가장 처음 (값을 처음 넣을 때)
#         return start
#     elif start - end == 0: # 마지막 node에서 마지막 node의 앞에 넣을 것인가 뒤에 넣을 것인가
#         if queue[start] > data:
#             return start
#         else:
#             return start + 1
        
    
#     mid = int((start + end)/2)
    
#     if queue[mid] < data:
#         return binary_search(queue, data, mid + 1, end)
#     elif queue[mid] > data:
#         return binary_search(queue, data, start, mid)
#     else:
#         return binary_search(queue, data, mid, mid)

# if __name__ == "__main__":
#     num = int(sys.stdin.readline())
#     queue = deque()
#     leng = 0

#     data = []
#     for _ in range(num):
#         data.append(int(input()))
    
#     save_stack = []
#     for dt in data:
#         input_index = binary_search(queue, dt, 0, leng-1)
#         mid = int((leng-1)/2)

#         if input_index < mid:
#             for _ in range(input_index):
#                 save_stack.append(queue.popleft())
#             queue.appendleft(dt)
#             for _ in range(input_index):
#                 queue.appendleft(save_stack.pop())
#         else:
#             for _ in range(leng - input_index):
#                 save_stack.append(queue.pop())
#             queue.append(dt)
#             for _ in range(leng - input_index):
#                 queue.append(save_stack.pop())
#         leng += 1
#         print(queue[int((leng-1)/2)])



import sys
import heapq

if __name__ == "__main__":
    num = int(sys.stdin.readline())

    heap_left = []
    heap_right = []
    for _ in range(num):
        if len(heap_left) == len(heap_right):
            heapq.heappush(heap_left, -int(sys.stdin.readline()))
        else:
            heapq.heappush(heap_right, int(sys.stdin.readline()))
        
        if len(heap_right) == 0:
            print(-heap_left[0])
            continue
        if -heap_left[0] > heap_right[0]:
            temp1 = -heapq.heappop(heap_left)
            temp2 = heapq.heappop(heap_right)
            heapq.heappush(heap_left, -temp2)
            heapq.heappush(heap_right, temp1)
        
        print(-heap_left[0])
    
    