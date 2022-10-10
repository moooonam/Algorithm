from collections import deque

dx=[0,1,0,-1] # 4방탐색
dy=[1,0,-1,0]

N =int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
for water in range(0,101): 
    visited= [[0]*N for _ in range(N)] # 방문 표시할 2차원 리스트
    cnt=0
    for i in range(N):
        for j in range(N):
            if arr[i][j] >water and visited[i][j]==0: # 높이보다 큰곳이 있으면 4방탐색해서 그부분을 표시할거
                q = deque()
                q.append((i,j))
                # print(water,i,j)
                visited[i][j]=1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if 0<= nx <N and 0<= ny <N and visited[nx][ny]==0 and arr[nx][ny] > water:
                            visited[nx][ny] =1
                            q.append((nx,ny))
                
                cnt+=1 # q로 끝까지 탐색하고 나왔으면 카운트 추가
    if cnt >max_v:
        max_v=cnt
print(max_v)
                    




