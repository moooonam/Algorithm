T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input()))for _ in range(N)]
    cha =N//2
    ans = 0
    for i in range(N):
        for j in range(N):
            if abs(i-cha)+abs(j-cha)<=cha:
                ans+=arr[i][j]
    print(f'#{tc} {ans}')