def f(day, price): # 상담이 끝났을 때의 일 수, 그 떄까지의 금액
    global max_price
    if day == N-1: # 마지막날 상담이 끝났으면 그대로 종료
        if price > max_price:
            max_price = price
    else:
        flag = False
        for i in range(day+1, N): # 상담이 끝난 다음날 부터
            if i + schedule[i][0]-1 < N:
                f(i + schedule[i][0]-1, price + schedule[i][1])
                flag = True
        if not flag:    # 상담이 끝난 다음날 부터 할 수 있는 상담이 없을 경우
            if price > max_price:
                max_price = price

N = int(input())
schedule = []
for _ in range(N): # 스케줄 배열 만들기 (인덱스 관계로 일 수를 하나씩 빼줌// N+1일 째 퇴사 -> N일 쨰 퇴사)
    T, P = map(int, input().split())
    schedule.append([T, P])
max_price = 0
for i in range(0, N):
    if i + schedule[i][0]-1 < N: # 처음 상담할 수 있는 날짜를 고르는 과정(Ti가 끝났을 때 N일 째 이내여야 한다.
        f(i + schedule[i][0]-1, schedule[i][1])
print(max_price)