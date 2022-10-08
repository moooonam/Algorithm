from collections import deque

dx=[0,1,0,-1] # 4방탐색
dy=[1,0,-1,0]

def gogo(): 
    while q:
        x, y, hap =q.popleft()

        # if x==N-1 and y==N-1:
        #     if hap < min_V:
        #         min_V= hap
        #     continue
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx<N and 0<=ny<N and hap+arr[nx][ny] < hap_arr[nx][ny] and hap+arr[nx][ny]<hap_arr[N-1][N-1]:
                hap_arr[nx][ny]=hap+arr[nx][ny]
                q.append((nx,ny,hap+arr[nx][ny]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,list(input()))) for _ in range(N)]
    q = deque()
    visited=[(0,0)]
    q.append((0,0,0))
    inf=1000000000
    hap_arr = [[inf]*(N) for _ in range(N)]
    gogo()
    # print(hap_arr)
    print(f'#{tc} {hap_arr[N-1][N-1]}')