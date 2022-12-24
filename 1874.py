
num = int(input())

data = []
for i in range(0, num):
    in_data = int(input())
    data.append(in_data)

stack = []
stack_data = 1

stack_forward = []
def input(a):
    stack.append(a)
    stack_forward.append("+")

def output(a):
    pop_data = stack.pop()
    if pop_data == a:
        stack_forward.append("-")
    else:
        stack.append(a)
        stack_forward.append("NO")

data_comduct = 0
success = 1
while data_comduct < len(data):
    if data[data_comduct] >= stack_data:
        while data[data_comduct] >= stack_data:
            input(stack_data)
            stack_data += 1
        output(data[data_comduct])
    elif data[data_comduct] < stack_data:
        output(data[data_comduct])

    if stack_forward[len(stack_forward)-1] == "NO":
        success = 0
        print("NO")
        break
    data_comduct += 1

if success == 1:
    for i in range(0, len(stack_forward)):
        print(stack_forward[i])

