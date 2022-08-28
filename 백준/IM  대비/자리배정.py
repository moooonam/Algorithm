c, r = map(int, input().split())
g = int(input())
me =True
sit = [[0]*(c+1) for _ in range(r+1)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
sit[1][1]=1
ni=1
nj=1
cnt=1
if g>c*r:
    print(0)
else:
    while me:
        for k in range(4):
            while True:
                ni += di[k]
                nj += dj[k]
                if 1<=ni <=r and 1<=nj <=c and sit[ni][nj]==0:
                    cnt+=1
                    sit[ni][nj]=cnt
                else:
                    ni -= di[k]
                    nj -= dj[k]
                    break
                if cnt == g:
                    print(nj, ni)
                    me=False
                    break


# 답은 맞는거 같은데