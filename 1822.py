num1, num2 = map(int, input().split())

num1_data = list(map(int, input().split()))
num2_data = list(map(int, input().split()))

num_result = list(set(num1_data) - set(num2_data))

len_result = len(num_result)
print(len_result)

if len_result > 0:
    num_result.sort()
    for i in num_result:
        print(i, end=" ")
