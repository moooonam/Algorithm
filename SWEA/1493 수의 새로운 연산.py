arr = [[0]*1000 for _ in range(1000)]
start=1
more=0
for i in range(1,1000):    
    more=i+1
    start+=i-1
    for j in range(1,1000):
        if j>=2:
            arr[i][j]=arr[i][j-1]+more
            more+=1
        else:
            arr[i][j]=start
T = int(input())
for tc in range(1, T+1):
    x1=y1=x2=y2=0
    p, q = map(int, input().split())
    for i in range(1,1000):
        for j in range(1,1000):
            if arr[i][j]==p:
                x1=i
                y1=j
            if arr[i][j]==q:
                x2=i
                y2=j
            if x1!=0 and x2!=0:
                break
        if x1!=0 and x2!=0:
                break
    print(f'#{tc} {arr[x1+x2][y1+y2]}')
