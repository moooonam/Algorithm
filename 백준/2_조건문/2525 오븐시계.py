#2525 오븐시계
A, B = map(int,input().split())
C = int(input())
resultA = (A+((B+C)//60))%24
resultB = (B+C)%60
print(resultA,resultB)