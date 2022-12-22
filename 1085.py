
x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

list_dis = []
list_dis.append(x)
list_dis.append(y)
list_dis.append(w-x)
list_dis.append(h-y)

print(min(list_dis))
