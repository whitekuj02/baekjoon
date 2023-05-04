def divide(arr):
    size = len(arr)
    answer = ''

    for i in range(size):
        for j in range(size):
            if arr[0][0] != arr[i][j]:
                cutleftup=[]
                for i in range(len(arr)//2):
                    tmp=[]
                    for j in range(len(arr[0])//2):
                        tmp.append(arr[i][j])
                    cutleftup.append(tmp)

                answer += divide(cutleftup)

                cutrightup=[]
                for i in range(len(arr)//2):
                    tmp=[]
                    for j in range(len(arr[0])//2,len(arr[0])):
                        tmp.append(arr[i][j])
                    cutrightup.append(tmp)
                answer += divide(cutrightup)

                cutleftdown=[]
                for i in range(len(arr)//2,len(arr)):
                    tmp=[]
                    for j in range(len(arr[0])//2):
                        tmp.append(arr[i][j])
                    cutleftdown.append(tmp)
                answer += divide(cutleftdown)

                cutrightdown=[]
                for i in range(len(arr)//2,len(arr)):
                    tmp=[]
                    for j in range(len(arr[0])//2,len(arr[0])):
                        tmp.append(arr[i][j])
                    cutrightdown.append(tmp)
                answer += divide(cutrightdown)

                answer= '('+answer+')'
                return answer
    else:
        return arr[0][0]


n=int(input())
arr=[]

for i in range(n):
    arr.append(list(input()))

print(divide(arr))