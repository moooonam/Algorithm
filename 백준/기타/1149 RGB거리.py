# 구글링 힌트 얻음 ...
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1,N):
    arr[i][0] += min(arr[i-1][1],arr[i-1][2])
    arr[i][1] += min(arr[i-1][0],arr[i-1][2])
    arr[i][2] += min(arr[i-1][0],arr[i-1][1])
ans = min(arr[N-1][0],arr[N-1][1],arr[N-1][2])
print(ans)

