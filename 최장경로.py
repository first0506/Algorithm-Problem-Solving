def dfs(a):
    global used, ans
    for i in range(N+1):
        if not used[i] and arr[a][i]:
            used[i] = 1
            dfs(i)
            used[i] = 0
    if sum(used) > ans:
        ans = sum(used)

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    ans = 0
    used = [0]*(N+1)
    for i in range(1, N+1):
        used[i] = 1
        dfs(i)
        used[i] = 0
    print("#{} {}".format(test_case, ans))




def bfs(i):
    global ans
    v = [0]*(N+1)
    v[i] = 1
    queue = [[i, 1, v]]
    while queue:
        a, length, used = queue.pop(0)
        for b in range(1, N+1):
            if not used[b] and arr[a][b]:
                used[b] = 1
                queue.append([b, length+1, used[:]])
                used[b] = 0
    if length > ans:
        ans = length

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    ans = 0
    for i in range(1, N+1):
        bfs(i)
    print("#{} {}".format(test_case, ans))