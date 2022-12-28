import math
import sys
from collections import Counter

input = sys.stdin.readline

num = int(input())
data = []
min = 4001
sum_ = 0
for i in range(0, num):
    a = int(input())
    sum_ += a
    data.append(a)

data.sort()

dic = Counter(data)

sorted_dic = dic.most_common()

eq = []

for i in sorted_dic:
    if i[1] == sorted_dic[0][1]:
        eq.append(i)

if len(eq) > 1:
    eq.sort(key=lambda x: x[0], reverse=False)
    max_common = eq[1][0]

else:
    max_common = eq[0][0]


f = round(sum_ / num)
print(f)
print(data[num // 2])
print(max_common)
print(abs(data[0] - data[-1]))