T = int(input())
for test_case in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    sutime = list(map(int, input().split()))    # 접수진행시간
    bitime = list(map(int, input().split()))    # 정비진행시간
    arrival = list(map(int, input().split()))   # 고객도착시간
    su = [0] * N    # 각 접수 창구별 완료시간
    su_finish = [[0, 0, 0] for _ in range(K)] # [고객번호, 접수완료시간, 접수 창구번호]
    bi = [0] * M    # 각 정비 창구별 완료시간
    bi_finish = [0] * K # 고객별 정비창구 이용번호
    for i in range(K):  # 고객 도착 시간순으로
        for j in range(len(su)):    # 고객이 접수할 수 있는 창구가 있을 때
            if arrival[i] >= su[j]: # 접수창구의 완료시간이 고객 도착시간과 같거나 빠를 때
                su[j] = arrival[i] + sutime[j]  # 접수창구 완료시간 증가
                su_finish[i] = [i, su[j], j]    # 고객별 접수완료 정보 저장
                break
        else:    # 고객이 접수할 수 있는 창구가 없어 기다릴 때
            for j in range(len(su)):
                if su[j] == min(su):    # 접수가 가장 빨리 완료되는 창구에 간다.
                    su[j] += sutime[j]  # 접수창구 완료시간 증가
                    su_finish[i] = [i, su[j], j]    # 고객별 접수완료 정보 저장
                    break

    for i in range(len(su_finish)-1):    # 저장된 고객별 접수완료 정보를 접수완료시간, 접수창구번호 순으로 정렬(선택정렬)
        min_su = i
        for j in range(i+1, len(su_finish)):
            if su_finish[j][1] < su_finish[min_su][1]:
                min_su = j
            elif su_finish[j][1] == su_finish[min_su][1]:
                if su_finish[j][2] < su_finish[min_su][2]:
                    min_su = j
        su_finish[i], su_finish[min_su] = su_finish[min_su], su_finish[i]

    for i in su_finish: # 정비창구에 도착하는 순서대로
        for j in range(len(bi)): # 정비창구에 대기가 필요 없을 때
            if i[1] >= bi[j]:   # 접수창구완료 시간이 정비창구 시간보다 같거나 클 때
                bi[j] = i[1] + bitime[j]    # 정비완료시간 증가
                bi_finish[i[0]] = j # 고객번호별 정비창구 번호 저장
                break
        else:    # 정비창구에 대기가 필요할 때
            for j in range(len(bi)):
                if bi[j] == min(bi):
                    bi[j] += bitime[j]
                    bi_finish[i[0]] = j
                    break

    cnt = 0
    for i in su_finish: # 창구 번호 비교
        if i[2] == A-1 and bi_finish[i[0]] == B-1: # 고객번호를 0번부터 시작해 A,B에 1 씩 뺴준다.
            cnt += i[0]+1   # 고객번호를 0번부터 시작해 1을 더해준다.
    if not cnt:
        print('#{} -1'.format(test_case))
    else:
        print('#{} {}'.format(test_case, cnt))