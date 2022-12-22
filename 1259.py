
data = []
num = 0
while 1:
    in_data = input()
    if in_data == '0':
        break
    data.append(in_data)
    num += 1

data_compare = []
for i in range(0, num):
    data_reverse = data[i][::-1]
    if data_reverse == data[i]:
        data_compare.append("yes")
    else:
        data_compare.append("no")
    print(data_compare[i])