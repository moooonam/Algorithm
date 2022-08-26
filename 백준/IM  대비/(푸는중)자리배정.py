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
ansx =0
ansy =0
while me:
    for k in range(4):
        while True:
            ni += di[k]
            nj += dj[k]
            if 1<=ni <=r and 1<=nj <=c:
                cnt+=1
                sit[ni][nj] = cnt
                if cnt == g:
                    ansx=ni
                    ansy=nj
                    me =False
                    print(ansx, ansy)
                    break
            else:
                ni -= di[k]
                nj -= dj[k]
                break
    if cnt== g:
        print(0)
        me = False



# 0 나올 조건이랑 추가해야해...