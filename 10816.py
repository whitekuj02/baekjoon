import sys
from collections import Counter

num = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

num2 = int(sys.stdin.readline())
data2 = list(map(int, sys.stdin.readline().split()))

# m = [x for x in data if x in data2]
# dic = Counter(m)
# sorted_dic = dic.most_common()
# for i in data2:
#     for k in sorted_dic:
#         if k[0] == i:
#             print(k[1], end=" ")
#             break
#     else:
#         print(0, end=" ")

def binary_search_left(arr, target, start, end, arr_length):
    if start > end:
        return 0

    mid = (start + end) // 2

    if arr[mid] == target and (mid-1 < 0 or arr[mid-1] != target):
        return mid
    elif arr[mid] >= target:
        end = mid - 1
    elif arr[mid] < target:
        start = mid + 1


    return binary_search_left(arr, target, start, end, arr_length)

def binary_search_right(arr, target, start, end, arr_length):
    if start > end:
        return 0

    mid = (start + end) // 2

    if arr[mid] == target and (mid+1 >= arr_length or arr[mid+1] != target):
        return mid + 1
    elif arr[mid] > target:
        end = mid - 1
    elif arr[mid] <= target:
        start = mid + 1

    return binary_search_right(arr, target, start, end, arr_length)

data.sort()
length = len(data)
for i in data2:
    print(binary_search_right(data, i, 0, length-1, length) -
          binary_search_left(data, i, 0, length-1, length), end=" ")