a, b, v = map(int,input().split())
# 시간초과!!!
# now=0
# cnt=0
# while True:
#     cnt+=1
#     now+=A
#     if now>= V:
#         break
#     now-=B
# print(cnt)
ans=(v-b)/(a-b)
if ans%1!=0:
    ans=int(ans)+1
print(int(ans))

