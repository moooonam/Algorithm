vin=[[0]*14 for _ in range(15)]
for s in range(14):
    vin[0][s]=s+1
for i in range(1, 15):
    vin[i][0]=1
    for j in range(1,14):
            vin[i][j]=vin[i][j-1]+vin[i-1][j]
T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())
    print(vin[k][n-1])