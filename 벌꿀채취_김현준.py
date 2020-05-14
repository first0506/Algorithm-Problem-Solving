def honey(i1, j1, i2, j2):
    global max_profit
    a, b = [], []       # 첫번째, 두번쨰 벌통의 수익들
    for m in range(j1, j1 + M):
        a.append(arr[i1][m])
    for m in range(j2, j2 + M):
        b.append(arr[i2][m])
    Aprofit = 0
    if sum(a) <= C:
        for k in a:
            Aprofit += k ** 2
    else:
        for i in range(1, (1<<M)-1):   # 첫번째 벌통 모든 부분집합 구하기
            A = []
            for j in range(M):
                if i & (1<<j):
                    A.append(a[j])
            if sum(A) <=C:   # 최대 양 C보다 작을 때
                profit = 0
                for k in A:
                    profit += k**2
                if profit > Aprofit:
                    Aprofit = profit
    Bprofit = 0
    if sum(b) <= C:
        for k in b:
            Bprofit += k ** 2
    else:
        for i in range(1, (1<<M)-1): # 두번째 벌통 모든 부분집합 구하기
            B = []
            for j in range(M):
                if i & (1 << j):
                    B.append(b[j])
            if 0 < sum(B) <= C: # 최대 양 C보다 작을 떄
                profit = 0
                for k in B:
                    profit += k ** 2
                if profit > Bprofit:
                    Bprofit = profit
    if Aprofit + Bprofit > max_profit:
        max_profit = Aprofit + Bprofit

T= int(input())
for test_case in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_profit = 0
    for i1 in range(N):
        for j1 in range(N):
            if j1+M-1 < N:  # 첫번쨰 일꾼이 가능한 벌통을 선택, M 길이의 벌통이 가능한지
                for i2 in range(i1, N):
                    if i2 == i1 and j1+M <N:    # 두번째 일꾼의 벌통이 첫번쨰 일꾼의 벌통과 같은 행에 있을 때
                        for j2 in range(j1+M, N):
                            if j2+M-1 <N:   # M 길이의 벌통이 가능한지
                                honey(i1, j1, i2, j2)   # 첫번쨰 일꾼과 두번쨰 일꾼의 맨 왼쪽 벌통 좌표
                    elif i2 != i1:  # 첫번쨰 일꾼의 벌통과 다른 행에 있을 때
                        for j2 in range(N):
                            if j2+M-1 <N:   # M 길이의 벌통이 가능한지
                                honey(i1, j1, i2, j2)   # 첫번쨰 일꾼과 두번쨰 일꾼의 맨 왼쪽 벌통 좌표
    print('#{} {}'.format(test_case, max_profit))