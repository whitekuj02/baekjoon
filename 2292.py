num = int(input())

# 1 7   19     37
# 1 1+6 1+6+12 1+6+12+18

i = 1
a = num -1
count = 1
while True:
    if i > a:
        break

    i += 6*count
    count += 1

print(count)