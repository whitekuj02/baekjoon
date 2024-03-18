
if __name__ == "__main__":
    s_list = []
    while(1):
        try:
            s = input()
            s_list.append(s)
        except:
            break
    
    for s in s_list:
        print(s)