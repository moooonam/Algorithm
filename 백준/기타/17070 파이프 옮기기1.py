# 가로 1 대각선 2 세로 3
# dx1=[0,1]
# dy1=[1,1]

# dx2=[0,1,1]
# dy2=[1,1,0]

# dx3=[1,1]
# dy3=[0,1]

def go(x,y,direc):
    global cnt,N
    if x==N-1 and y==N-1:
        cnt+=1
        return
    if direc ==1:
        if 0<=x+1<N and 0<=y+1<N and arr[x+1][y+1] ==0 and arr[x+1][y] ==0 and arr[x][y+1] ==0:
            go(x+1,y+1,2)
        if 0<=x<N and 0<=y+1<N and arr[x][y+1] ==0:
            go(x,y+1,1)

    elif direc ==2:
        if 0<=x+1<N and 0<=y+1<N and arr[x+1][y+1] ==0 and arr[x+1][y] ==0 and arr[x][y+1] ==0:
            go(x+1,y+1,2)
        if 0<=x<N and 0<=y+1<N and arr[x][y+1] ==0:
            go(x,y+1,1)
        if 0<=x+1<N and 0<=y<N and arr[x+1][y] ==0:
            go(x+1,y,3)

    elif direc ==3:
        if 0<=x+1<N and 0<=y+1<N and arr[x+1][y+1] ==0 and arr[x+1][y] ==0 and arr[x][y+1] ==0:
            go(x+1,y+1,2)
        if 0<=x+1<N and 0<=y<N and arr[x+1][y] ==0:
            go(x+1,y,3)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt =0
go(0,1,1)
print(cnt)