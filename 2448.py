num = int(input())

def pattern(num):
    if num == 3:
        a = ["  *  ", " * * ", "*****"]
        return a

    star = pattern(num//2)
    stars = []

    for i in star:
        stars.append(" "*(num//2) + i + " "*(num//2))
    for i in star:
        stars.append(i + " " + i)

    return stars

star = pattern(num)
print("\n".join(star))