from collections import deque

def RGB():
    global min_V
    while q:
        row, col, hap = q.popleft()
        # print(row,col,hap)
        if hap > min_V:
            continue
        if row ==N-1:
            if hap< min_V:
                min_V = hap
            continue
        
        for i in range(3):
            if i != col:
                q.append((row+1,i,hap+arr[row+1][i]))
        

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_V = 100000000
q= deque()
q.append((0,0,arr[0][0]))
q.append((0,1,arr[0][1]))
q.append((0,2,arr[0][2]))
RGB()
print(min_V)