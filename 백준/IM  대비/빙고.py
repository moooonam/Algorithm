#딕셔너리를 쓰면 차암 좋을거 같은데 뭘 알아야 쓰지
# 개 잘했으~~
def bingo_cnt(arr):
    #가로찾기
    cnt = 0
    
    for i in range(5):
        a = 0
        for j in range(5):
            a += arr[i][j]
        if a ==0:
            cnt += 1
    #세로 찾기
    for i in range(5):
        b = 0
        for j in range(5):
            b += arr[j][i]
        if b == 0:
            cnt += 1
    # 대각선 찾기
    c=0
    for i in range(5):
        c +=arr[i][i]
    if c ==0:
        cnt+=1
    d=0        
    for i in range(5):    
        d += arr[i][4-i]
    if d == 0:
        cnt+=1
    return cnt


my_arr = [list(map(int, input().split()))for _ in range(5)]
call = [list(map(int, input().split()))for _ in range(5)]
for i in range(2):
    for j in range(5):
        callnum= call[i][j]
        for x in range(5):
            for y in range(5):
                if my_arr[x][y] == callnum:
                    my_arr[x][y] = 0
                    break
ans=10
for i in range(2,5,1):
    for j in range(5):
        callnum = call[i][j]
        for x in range(5):
            for y in range(5):
                   if my_arr[x][y] == callnum:
                    my_arr[x][y] = 0
                    ans+=1
                    break
        if bingo_cnt(my_arr) >2:
            break
    if bingo_cnt(my_arr) >2:
        break
print(ans)                
