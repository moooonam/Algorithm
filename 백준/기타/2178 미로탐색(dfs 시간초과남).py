# dfs로 했더니 테스트 케이스틑 대충 다 맞는데 시간초과

dx=[0,1,0,-1]
dy=[1,0,-1,0]
def gogo(x,y,cnt):
    global N, M, min_cnt
    if cnt> min_cnt:
        return 
    if x==N-1 and y==M-1:
        if cnt+1 < min_cnt:
            min_cnt=cnt+1
        return min_cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # print(nx,ny)
        if 0<= nx <N and 0<= ny <M:
            if miro[nx][ny]=='1' and (nx,ny) not in visited :
                visited.append((nx,ny))
                gogo(nx,ny,cnt+1)
                visited.pop()



N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)]
min_cnt =9999999999
visited=[(0,0)]
gogo(0,0,0)
print(min_cnt)