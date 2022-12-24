import math
have_num, need_num = input().split()

have_num = int(have_num)
need_num = int(need_num)

data = []
min = float(1)
max = float(1)
for i in range(0, have_num):
    in_data = int(input())
    data.append(in_data)
    if in_data > max:
        max = in_data

def check(num):
    count = 0
    for i in range(0,have_num):
        count += math.floor(data[i]/num)
        if count >= need_num:
            return True
    return False

result = 1
while min <= max:
    mid = math.floor((min+max)/2)
    if check(mid):
        if result < mid:
            result = mid
        min = mid +1
    else:
        max = mid -1


print(result)

