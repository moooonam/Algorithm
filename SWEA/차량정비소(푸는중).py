T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    jubsu_time = list(map(int, input().split())) #접수시간
    jubsu_time.insert(0,0)
    jubsu =[0]*N # 접수창구 상태
    jungbee_time = list(map(int, input().split())) #정비시간
    jungbee_time.insert(0,0)
    jungbee = [0]*M #정비창구 상태
    arrival = list(map(int, input().split())) #고객 도착 시간
    arrival.insert(0,0)
    compl =[] #일 다본사람 넣을거
    pick =[[0]*(N+1) for _ in range(M+1)] # i행 j열에다가 완료한사람 번호를 더해줄거다
    waiting_1 = [] # 접수창구 기다리는 사람 
    waiting_2 = [] # 정비창구 기다리는 사람
    time = 0 #지금 시간
    in_num =1 #지금까지 들어간 사람 수-1 (검사해야할 순번)
    while len(compl) < K:
        # 도착한사람 waiting_1에 넣어주기
        for i in range(in_num, len(arrival)):
            if arrival[i] == time:
                waiting_1.append(i)
            else:
                in_num = i #다음에 검사해야할 시작사람
                break
        
    # print(len(pick))
    
    # print(jubsu)
    # print(jungbee)
