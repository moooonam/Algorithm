N = int(input())
arr = [[0]*1002 for _ in range(1002)]
for n in range(1,N+1):
    x1,y1,s,h = map(int, input().split())
    for i in range(x1, x1+s):
        for j in range(y1, y1+h):
            arr[i][j] = n
for k in range(1,N+1):
    cnt = 0
    for i in range(1002):
        for j in range(1002):
            if arr[i][j] == k:
                cnt +=1
    print(cnt)
# 왜 성공 안뜨는지 모르겠음
    # 아마 시간 초과인듯

