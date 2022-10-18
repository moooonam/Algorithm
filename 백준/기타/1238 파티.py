# 다익스트라 구글링함... ㅠㅠㅠㅠㅠㅠ


INF = int(1e9)
N, M, X = map(int, input().split())
graph=[[] for _ in range(N+1)]
graph_come=[[] for _ in range(N+1)]
for _ in range(M):
    i, j, v = map(int,input().split())
    graph[i].append((j, v))
    graph_come[j].append((i, v))
distance =[INF]*(N+1)
visited=[0]*(N+1)

def di(start,graph):
    distance[start] =0
    visited[start] =1
    for i in graph[start]:
        distance[i[0]] =i[1]
    for _ in range(N-1):
        now=0
        min_v = INF
        for i in range(1,N+1):
            if visited[i]==0 and distance[i] < min_v:
                min_v = distance[i]
                now =i
        visited[now] = 1 
        for next in graph[now]:
            cost = distance[now] +next[1]
            if cost < distance[next[0]]:
                distance[next[0]]= cost
di(X,graph)
hap=distance
distance =[INF]*(N+1)
visited=[0]*(N+1)
di(X,graph_come)
ans=0
for i in range(1,N+1):
    hap[i]+=distance[i]
    if hap[i] >ans:
        ans = hap[i]
print(ans)
