def swim(c, money):
    global ans
    if money > ans:
        return
    else:
        if c < 12:
            flag = False
            for i in range(c, len(plans)):
                if plans[i]:
                    flag = True
                    for k in range(3):
                        if k == 0:
                            swim(i+1, money + cost[0]*plans[i])
                        elif k == 1:
                            swim(i+1, money + cost[1])
                        elif k == 2:
                            swim(i+3, money + cost[2])
                    break
            if not flag:
                ans = money
        else:
            ans = money

T = int(input())
for test_case in range(1, T+1):
    cost = list(map(int, input().split()))
    plans = list(map(int, input().split()))
    ans = cost[3]
    swim(0, 0)
    print('#{} {}'.format(test_case, ans))



# 선생님 수업
def f(n, s, d, m, m3):
    global minV
    if n>12:
        if minV > s:
            minV = s
    elif minV <= s:
        return
    else:
        f(n+1, s+table[n]*d, d, m, m3)      #n월에 1일 이용권
        f(n+1, s+m, d, m, m3)               #n월에 1달 이용권
        f(n+3, s+m3, d, m, m3)              #n월에 3달 이용권
T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())     # 이용권 비용
    table = [0]+list(map(int, input().split()))     # 월별 이용일
    minV = y    # 1년 이용권 비용
    f(1, 0, d, m, m3)       # 1월부터 고려
    print('#{} {}'.format(tc, minV))