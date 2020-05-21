from collections import deque
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    graph = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        graph[nums[i*2]][nums[i*2+1]] = 1
        graph[nums[i*2+1]][nums[i*2]] = 1
    v=[0]*(N+1)
    ans = 0
    for i in range(1, N+1):
        if not v[i]:
            ans = ans+1
            q=deque([i])
            while q:
                n = q.popleft()
                for k in range(1, N+1):
                    if graph[n][k] and not v[k]:
                        v[k]=1
                        q.append(k)
    print('#{} {}'.format(test_case, ans))