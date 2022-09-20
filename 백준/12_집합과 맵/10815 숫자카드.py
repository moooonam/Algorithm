N = int(input())
sang=set(map(int, input().split()))
M = int(input())
check=list(map(int,input().split()))
# 또 시간초과, #set으로 했더니 통과
for i in check:
    if i in sang:
        print(1, end=' ')
    else:
        print(0, end=' ')

