N = int(input())
arr = list(map(int, input().split()) )
rearr = sorted(arr)
ans = 0
for i in rearr:
    ans += i*N
    N-=1
print(ans)