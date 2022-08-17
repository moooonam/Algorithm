N = int(input())
for i in range(N):
    b = 0
    ans = 0
    c = str(i)
    for j in range(len(c)):
        b += int(c[j])
    if i+b == N and b != 0:
        ans = i
        break
print(ans)

