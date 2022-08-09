# N = int(input())
# count=0
# for i in range(N):
#     word=list(input())
#     if len(word)<3:
#         count+=1
#     elif len(word)==3:
#         if word[0]!=word[1] and word[0]==word[1]:
#             continue
#     else:
#         a= True
#         while a:
#             for j in range(len(word)-1):
#                 if word[j]!=word[j+1]:
#                     for l in range(len(word)-1,j+1,-1):
#                         if word[j]==word[l]:
#                             a=False
#                             break
                
#             else:
#                 count+=1
# print(count)
#----- j,j+1이 다르고 j+2부터 끝까지 중에 j랑 같은게 있으면 그룹단어가 아니니까 탈락 이렇게 생각함
# 결국 1시간동안 못하고 구글링 슬쩍 함
N = int(input())
count=N
for i in range(N):
    word= input()
    for j in range(0, len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count-=1
            break
print(count)