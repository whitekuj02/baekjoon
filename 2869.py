A, B, V = map(int, input().split())

num = (V-A)%(A-B)
if num > 0:
    day = (V-A)//(A-B) + 2
else:
    day = (V-A) // (A - B) + 1
print(int(day))