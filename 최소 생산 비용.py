def dfs(i):
    global ans, cost
    if i==N:
        if cost < ans:
            ans = cost
    elif cost < ans:
        for k in range(N):
            if not v[k]:
                v[k] = 1
                cost += arr[i][k]
                dfs(i+1)
                cost -= arr[i][k]
                v[k] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 2**31-1
    cost = 0
    v = [0]*N
    dfs(0)
    print('#{} {}'.format(test_case, ans))