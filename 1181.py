num = int(input())

data = []
for i in range(0, num):
    in_data = input()
    data.append(in_data)

data = list(set(data))
num = len(data)
def marge_sort(b,c):
    sort = []
    b_idx = 0
    c_idx = 0
    while not(b_idx == len(b) or c_idx == len(c)):
        if len(b[b_idx]) > len(c[c_idx]):
            sort.append(c[c_idx])
            c_idx += 1
        elif len(b[b_idx]) < len(c[c_idx]):
            sort.append(b[b_idx])
            b_idx += 1
        else:
            if b[b_idx] > c[c_idx]:
                sort.append(c[c_idx])
                c_idx += 1
            else:
                sort.append(b[b_idx])
                b_idx += 1

    if b_idx != len(b):
        for i in range(b_idx, len(b)):
            sort.append(b[i])
    else:
        for i in range(c_idx, len(c)):
            sort.append(c[i])
    return sort
def marge(a):
    if len(a) > 2:
        b = marge(a[:int(len(a)/2)])
        c = marge(a[int(len(a)/2):])
        return marge_sort(b, c)
    elif len(a) == 2:
        if len(a[0]) > len(a[1]):
            temp = a[1]
            a[1] = a[0]
            a[0] = temp
        elif len(a[0]) == len(a[1]):
            if a[0] > a[1]:
                temp = a[1]
                a[1] = a[0]
                a[0] = temp
        return a
    else:
        return a



# for i in range(0, num):
#     index = i
#     for k in range(i, num):
#         if len(data[index]) > len(data[k]):
#             index = k
#         elif len(data[index]) == len(data[k]):
#             if data[index] > data[k]:
#                 index = k
#
#     temp = data[i]
#     data[i] = data[index]
#     data[index] = temp

data = marge(data)
for i in range(0, num):
    print(data[i])