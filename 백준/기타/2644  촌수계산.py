from collections import deque

def chon(p):
    q = deque()
    q.append(p)
    while q:
        go_index= q.popleft()
        for i in arr[go_index]:
            if visited[i]==0:
                visited[i] = visited[go_index]+1 # 제일 처음 출발로부터 거리를 다 계산
                q.append(i)

N = int(input())
arr=[[] for _ in range(N+1)]
x,y = map(int,input().split()) # 비교할 두 번호
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b) # 양쪽다 이동이 가능 해야함
    arr[b].append(a)
# print(arr)
visited=[0]*(N+1)
chon(x)
if visited[y]==0:
    print(-1)
else:
    print(visited[y])



