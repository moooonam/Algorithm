N = int(input())
arr = [list(input().split()) for _ in range(N)]
for i in range(N):
    arr[i][0]=int(arr[i][0])
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if arr[j][0] > arr[j+1][0]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
for k in range(N):
    print(arr[k][0], end=" ")
    print(arr[k][1])

# 시간초과.....