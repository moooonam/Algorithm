N = int(input())
M = int(input())
arr = [list() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
ans = [1]
def search(x):
    for num in arr[x]:
        # print(num)
        if num not in ans:
            ans.append(num)
            search(num)
            
search(1)
print(len(ans)-1)