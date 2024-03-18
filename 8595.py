

if __name__ == "__main__":
    num = int(input())
    input_list = list(input())
    input_ASCII_list = list(map(ord, input_list))

    all_hidden_num = []
    int_list = []
    for i in range(0,num):
        if input_ASCII_list[i] > 47 and input_ASCII_list[i] < 58:
            int_list.append(input_list[i])
        else:
            if len(int_list) > 0 :
                all_hidden_num.append(int("".join(int_list)))
            int_list = []
    
    if len(int_list) > 0 :
        all_hidden_num.append(int("".join(int_list)))

    result = 0
    for i in all_hidden_num:
        result += i

    print(result)