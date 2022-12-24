num = int(input())

test_num_list = []
know_case_list = []
data_list = []
for _ in range(0, num):
    test_num, know_case = input().split()
    test_num = int(test_num)
    know_case = int(know_case)
    test_num_list.append(test_num)
    know_case_list.append(know_case)
    data = input().split()
    for i in range(0, len(data)):
        data[i] = int(data[i])
    data_list.append(data)


for i in range(0, num):
    print_num = 0
    while print_num < test_num_list[i]:
        if know_case_list[i] != 0:
            if data_list[i][0] < max(data_list[i]):
                data_list[i].append(data_list[i][0])
                data_list[i].pop(0)
            elif data_list[i][0] >= max(data_list[i]):
                data_list[i].pop(0)
                print_num += 1
            know_case_list[i] = (len(data_list[i])+ know_case_list[i] - 1) % len(data_list[i])
        else:
            if data_list[i][0] < max(data_list[i]):
                data_list[i].append(data_list[i][0])
                data_list[i].pop(0)
                know_case_list[i] = (len(data_list[i]) + know_case_list[i] - 1) % len(data_list[i])
            elif data_list[i][0] >= max(data_list[i]):
                data_list[i].pop(0)
                print_num += 1
                print(print_num)
                break
