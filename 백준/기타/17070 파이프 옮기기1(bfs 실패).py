# bfs로 풀었더니 70%쯤에서시간초과
from collections import deque
# 가로 1 대각선 2 세로 3
dx1=[0,1]
dy1=[1,1]

dx2=[0,1,1]
dy2=[1,1,0]

dx3=[1,1]
dy3=[0,1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr[0][0]==1
arr[0][1]==1
q =deque()
q.append((0,1,1))
cnt=0
while q:
    x,y,direc = q.popleft()
    if x==N-1 and y==N-1:
        cnt+=1
        continue

    if direc ==1:
        for i in range(2):
            if i==1:
                nx = x + dx1[i]
                ny = y + dy1[i]
                if  0<=nx<N and 0<=ny<N and arr[nx][ny] ==0 and arr[nx-1][ny] ==0 and arr[nx][ny-1] ==0:
                    q.append((nx,ny,2))
            else:
                nx = x + dx1[i]
                ny = y + dy1[i]
                if 0<=nx<N and 0<=ny<N and arr[nx][ny] ==0:
                    q.append((nx,ny,1))
    elif direc ==2:
        for i in range(3):
            if i==1:
                nx = x + dx2[i]
                ny = y + dy2[i]
                if 0<=nx<N and 0<=ny<N and arr[nx][ny] ==0 and arr[nx-1][ny] ==0 and arr[nx][ny-1] ==0:
                    q.append((nx,ny,2))
            else: 
                nx = x + dx2[i]
                ny = y + dy2[i]
                if 0<=nx<N and 0<=ny<N and arr[nx][ny] ==0:
                    if i==0:
                        q.append((nx,ny,1))
                    elif i==2:
                        q.append((nx,ny,3))
    elif direc ==3:
        for i in range(2):
            if i==1:
                nx = x + dx3[i]
                ny = y + dy3[i]
                if 0<=nx<N and 0<=ny<N and arr[nx][ny] ==0 and arr[nx-1][ny] ==0 and arr[nx][ny-1] ==0:
                    q.append((nx,ny,2))
            else:
                nx = x + dx3[i]
                ny = y + dy3[i]
                if 0<=nx<N and 0<=ny<N and arr[nx][ny] ==0:
                    q.append((nx,ny,3))

print(cnt)
