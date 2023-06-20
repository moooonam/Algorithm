dx = [1,0,-1,0]
dy = [0,1,0,-1]
def search(x,y):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and check_arr[nx][ny] == 0:
                    check_arr[nx][ny] = 1
                    stack.append((nx, ny))
    
T = int(input())
for _ in range(T):
    ans = 0
    M, N, K = map(int, input().split())
    check_arr = list([0]*M for __ in range(N))
    arr = list([0]*M for __ in range(N))
    for i in range(K):
        a,b = map(int, input().split())
        arr[b][a] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and check_arr[i][j] == 0:
                check_arr[i][j] = 1
                search(i,j)
                ans+=1
    print(ans)
