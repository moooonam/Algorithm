N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)
for i in range(1,N):
    for j in range(i+1):
        if j==0:
            arr[i][j] = arr[i][j] + arr[i-1][j]
        elif j == i:
            arr[i][j] = arr[i][j] + arr[i-1][j-1]
        else:
            arr[i][j] = arr[i][j] + max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[N-1])) 