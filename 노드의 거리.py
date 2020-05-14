def bfs(s):
    queue = [[s, 0]]
    visit = [0]*V
    visit[s] = 1
    while queue:
        i, length = queue.pop(0)
        if i==f-1:
            return length
        for j in range(V):
            if graph[i][j] and not visit[j]:
                queue.append([j, length+1])
                visit[j] = 1
    return 0

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*V for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1
    s, f = map(int, input().split())
    print('#{} {}'.format(test_case, bfs(s-1)))