num = int(input())

box3 = 0
box5 = 0

while box3*3 < num:
    if (num-box3*3) % 5 != 0:
        box3 += 1
    else:
        box5 = (num-box3*3) // 5
        print(box3 + box5)
        break
else:
    if box3*3 == num:
        print(box3)
    else:
        print(-1)
