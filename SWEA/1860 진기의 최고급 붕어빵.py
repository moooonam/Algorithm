T = int(input())
for tc in range(1, T+1):
    n, m, k =map(int, input().split())
    customer=list(map(int, input().split()))
    customer.sort()
    last_customer=max(customer)
    boong=0
    customer_num=0 # 받을 손님 인덱스
    ans = 'Possible'
    for i in range(0 ,last_customer+1):
        if i!=0 and i%m==0:
            boong +=k
        if i==customer[customer_num]:
            if boong!= 0:
                boong-=1
                customer_num+=1
            else:
                ans='Impossible'
                break
    print(f'#{tc} {ans}')

