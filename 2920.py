num = input().split()

num_0 = int(num[0])
num_1 = int(num[1])

no_asc = 0
no_desc = 0
if num_0 == num_1-1:
    for i in range(2, len(num)):
        if num_0 != int(num[i])-i:
            no_asc = 1
            print("mixed")
            break
    if no_asc == 0:
        print("ascending")
elif num_0 == num_1+1:
    for i in range(2, len(num)):
        if num_0 != int(num[i])+i:
            no_desc = 1
            print("mixed")
            break
    if no_desc == 0:
        print("descending")
else:
    print("mixed")







