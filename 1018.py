
row, col = input().split()
row = int(row)
col = int(col)

chese = []

for i in range(0, row):
    data = input()
    data_list = list(data)
    chese.append(data_list)

min_row = 0
min_col = 0
min_add = row * col
for cut_start_row in range(0, row - 7):
    for cut_start_col in range(0, col-7):
        add = [0, 0]
        for W in range(0, 2):
            # W == 0 :B start
            # W == 1 :W start
            compare_W = W
            for i in range(cut_start_row, cut_start_row+8):
                for j in range(cut_start_col, cut_start_col+8):
                    if compare_W == 1:
                        if chese[i][j] == 'B':
                            add[W] += 1
                    else:
                        if chese[i][j] == 'W':
                            add[W] += 1
                    compare_W = (compare_W+1) % 2
                compare_W = (compare_W+1) % 2

        #B or W start decide
        final_add = 0
        if add[0] > add[1]:
            final_add = add[1]
        else:
            final_add = add[0]

        if final_add < min_add:
            min_col = cut_start_col
            min_row = cut_start_row
            min_add = final_add

print(min_add)