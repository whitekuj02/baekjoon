num = int(input())

num_copy = 0
find = 0
while num_copy < num:
    a = list(map(int, str(num_copy)))
    b = num_copy + sum(a)

    if b == num:
        find = 1
        break
    else:
        num_copy += 1

if find == 1:
    print(num_copy)
else:
    print(0)