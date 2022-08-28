
A = int(input()) #스위치 수
swich = list(map(int, input().split())) #스위치
swich.insert(0, 0)
N = int(input()) # 개수
for i in range(N):
    x, y = map(int, input().split())
    cnt = 1
    if x == 1:#남자일때
        c=1
        for j in range(y,A+1,y):
            if swich[j] == 1:
                swich[j] = 0
            else:
                swich[j] = 1
            
    else: #여자일때
        if swich[y] == 1:
            swich[y] = 0
        else:
            swich[y] = 1
        while True:
            if y+cnt <=A and 1<= y-cnt and swich[y-cnt] == swich[y+cnt]:
                cnt+=1
                continue
            else:
                cnt-=1
                break
        if cnt !=0:
            for k in range(1, cnt+1):      
                if swich[y+k]==0:
                    swich[y+k]=1
                else:
                    swich[y+k]=0
                if swich[y-k]==0:
                    swich[y-k]=1
                else:
                    swich[y-k]=0
for i in range(1,A+1):
    print(swich[i], end =" ")
    if i%20==0:
        print()
 
# 후....