T = int(input())
for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    sum_list=[]
    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                sum_list.append(num_list[i]+num_list[j]+num_list[k])
    sum_list= set(sum_list)
    sum_list=list(sum_list)
    sum_list.sort()
    ans = sum_list[-5]
    print(f'#{tc} {ans}')