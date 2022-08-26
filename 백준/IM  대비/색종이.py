N = int(input())
vin = [[0]*101 for _ in range(101)]
cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            vin[a+i][b+j] +=1
   
for i in range(101):
    for j in range(101):
        if vin[i][j] !=0 :
            cnt+=1

print(cnt)