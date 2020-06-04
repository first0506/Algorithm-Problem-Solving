from collections import deque
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    v = [0]*(N+1)
    v[1] = 1
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    q = deque()
    q.append([1, 0])
    while q:
        friend, level = deque.popleft(q)
        if level==2:
            break
        for i in graph[friend]:
            if not v[i]:
                v[i] = 1
                q.append([i, level+1])
    print('#{} {}'.format(test_case, sum(v)-1))