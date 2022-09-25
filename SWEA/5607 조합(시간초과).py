def fac(n):
    if n <=1:
        return 1
    else:
       return n*fac(n-1)
T = int(input())
for tc in range(1, T+1):
    N, R = map(int, input().split())
    #재귀로 하려 했으나 시간초과..
    # ans = fac(N)//(fac(R)*fac(N-R))
    ans=1
    p =R
    for _ in range(R):
        ans*=N
        N-=1
    for _ in range(R):
        ans= ans//p
        p-=1
    print(f'#{tc} {ans}')
    

