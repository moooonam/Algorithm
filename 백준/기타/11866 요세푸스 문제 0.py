N, K = map(int, input().split())
ans =[]
arr = [i for i in range(1, N+1)] # 1부터 N까지 리스트
ind =0 # 빼줄 인덱스
while arr:
    ind +=K-1 #인덱스에 K-1 더하기(0부터니까 K-1)
    while ind >= len(arr): #인덱스가 길이보다 길면 작아질때까지 리스트 길이만큼 뺌
        ind-=len(arr)
    p = arr.pop(ind)# 제거하고
    ans.append(p)# 답에 추가
b= ", ".join(map(str,ans)) # 출력형식 맞추기
print(f'<{b}>')
    

