from collections import deque

dx=[0,1,0,-1] # 4방탐색
dy=[1,0,-1,0]
def gogo(x,y):
    global N, M, min_cnt,cnt
    while True:
        x,y,cnt = q.popleft() # 좌표와 카운트 꺼내기
        if cnt> min_cnt: # 이미 카운트가 민값보다 크면 그냥 진행 안시킴(가지치기)
            continue
        if x==N-1 and y==M-1: #도착지점에 도착하면 리턴
            if cnt+1 < min_cnt:
                min_cnt=cnt+1
            return min_cnt
        for i in range(4): # 사방탐색
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx,ny)
            if 0<= nx <N and 0<= ny <M:
                if miro[nx][ny]=='1' and (nx,ny) not in visited : # 아직 방문 안한 1 이면 q에 append
                    q.append((nx,ny,cnt+1))
                    visited.append((nx,ny)) # 방문 체크
                
                
N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)]
min_cnt =9999999999 # 대충 왕창 큰값
visited=[(0,0)] # 방문 여부 체크할 리스트
q=deque()
q.append((0,0,0))
cnt =1 # 출발점에서 1로 시작
gogo(0,0)
print(min_cnt)