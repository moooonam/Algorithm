T=int(input())
for tc in range(1, T+1):
    memo=list(map(int,input()))
    my=[0]*len(memo)
    cnt=0
    for i in range(len(memo)):
        if memo[i]!= my[i]:
            if my[i]==0:
                for j in range(i,len(memo)):
                    my[j]=1
            else:
                for j in range(i,len(memo)):
                    my[j]=0
            cnt+=1
        if memo==my:
            break
    print(f'#{tc} {cnt}')
