K = int(input())
row =[]
col =[]
for _ in range(6):
    a, b = map(int, input().split())
    if a==1 or a==2:
        row.append(b)
    else:
        col.append(b)
