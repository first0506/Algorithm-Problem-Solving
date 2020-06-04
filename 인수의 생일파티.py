from heapq import heappush, heappop
T = int(input())
for test_case in range(1, T+1):
    N, M, X = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        arr[a][b] = c
    goTime = [2**31-1]*(N+1)
    goTime[X] = 0
    backTime = [2**31-1]*(N+1)
    backTime[X] = 0
    q = []
    heappush(q, [0, X])
    while q:
        time, k = heappop(q)
        for i in range(1, N+1):
            if arr[i][k]:
                tmp = time+arr[i][k]
                if tmp < goTime[i]:
                    goTime[i] = tmp
                    heappush(q, [tmp, i])
    q = []
    heappush(q, [0, X])
    while q:
        time, k = heappop(q)
        for i in range(1, N+1):
            if arr[k][i]:
                tmp = time+arr[k][i]
                if tmp < backTime[i]:
                    backTime[i] = tmp
                    heappush(q, [tmp, i])
    ans = 0
    for i in range(1, N+1):
        tmp = goTime[i] + backTime[i]
        if tmp and ans < tmp:
            ans = tmp
    print('#{} {}'.format(test_case, ans))