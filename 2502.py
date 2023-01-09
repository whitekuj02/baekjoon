day, num = map(int, input().split())

day_1 = [1, 0]
day_2 = [0, 1]

# x y x+y x+2y 2x+3y 3x+5y 5x+8y
# 1 0  1   1     2     3     5
# 0 1  1   2     3     5     8

for i in range(2, day):
    day_1.append(day_1[i - 2] + day_1[i - 1])
    day_2.append(day_2[i - 2] + day_2[i - 1])

a = day_1[day-1]
b = day_2[day-1]

day_1_result = 1
day_2_result = 1
while True:
    find = num - a * day_1_result
    if find % b == 0:
        day_2_result = int(find / b)
        break
    day_1_result += 1


print(day_1_result)
print(day_2_result)