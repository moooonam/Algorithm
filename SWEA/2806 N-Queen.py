
def queen(x):
    global cnt
    if x==N:
        cnt+=1
        return
    for i in range(N):
      if visited_x[i]==0 and visited_xy[i+x]==0 and (x-i) not in visited_yx:
        visited_x[i]=1 
        visited_xy[x+i]=1 
        visited_yx.append(x-i)
        queen(x+1)
        visited_x[i]=0  
        visited_xy[x+i]=0 
        visited_yx.remove(x-i) 

T = int(input())
for tc in range(1,T+1):
    N= int(input())
    visited_x=[0]*N
    visited_xy=[0]*(N*2)
    visited_yx=[]
    cnt=0
    queen(0)
    print(f'#{tc} {cnt}')