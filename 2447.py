num = int(input())

length = num//3

def pattarn(num):
    if num == 1:
        min_star = ["*"]
        return min_star

    star = pattarn(num//3)
    stars = []

    for i in star:
        stars.append(i*3)
    for i in star:
        stars.append(i + " "*(num//3) + i)
    for i in star:
        stars.append(i*3)

    return stars

star = pattarn(num)

print("\n".join(star))