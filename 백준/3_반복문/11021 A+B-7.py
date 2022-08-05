N = int(input())
c=1
for i in range(N):
    a,b=map(int,input().split())
    result=a+b
    print(f'Case #{c}: {a} + {b} = {result}')
    c+=1