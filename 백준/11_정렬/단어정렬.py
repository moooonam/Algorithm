N = int(input())
arr = []

for i in range(N):
    arr.append(input())
arr =set(arr)
arr =list(arr)
cnt_list = list([] for _ in range(51))
for j in range(len(arr)):
    cnt_list[len(arr[j])].append(arr[j])
for i in range(51):
    for j in range(len(cnt_list[i])-1, 0, -1):
        for k in range(0,j):
            if cnt_list[i][k] > cnt_list[i][k+1]:
                cnt_list[i][k] , cnt_list[i][k+1] = cnt_list[i][k+1] ,cnt_list[i][k]
for i in range(51):
    for j in range(len(cnt_list[i])):
        print(cnt_list[i][j])

# 또 시간초과...
# 그냥 구글링해서 제출했음