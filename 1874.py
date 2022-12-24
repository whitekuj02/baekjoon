
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
    stack.pop(a)
    stack_forward.append("-")

while stack_data > num:



