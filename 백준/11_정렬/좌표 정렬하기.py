
N = int(input())
arr =[list(map(int, input().split())) for _ in range(N)]
ans = sorted(arr)
for i in range(N):
    print(ans[i][0], ans[i][1])