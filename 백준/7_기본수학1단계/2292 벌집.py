# x = int(input())
# n=2
# while True:
#     if x==1:
#         print(1)
#         break
#     elif -n<=(x-1)/3-n**2 <=n:
#         print(n+1)
#         break
#     else:
#         n+=1
# 또 시간초과... 검색 찬스를 썼다
x = int(input())
n=1
s=1
if x==1:
    print(1)
else:
    while True:
        if s >= x:
            print(n)
            break
        else: 
            s= s+6*n
            n+=1
