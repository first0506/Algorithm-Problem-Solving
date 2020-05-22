from heapq import heappush, heappop
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])
        adj[e].append([s, w])
    INF = float('inf')
    key = [INF]*(V+1)
    key[0] = 0
    mst = [0]*(V+1)
    result = 0
    q = []
    heappush(q, [0, 0])
    while q:
        w, s = heappop(q)
        if not mst[s]:
            mst[s] = 1
            result += w
            for end, weight in adj[s]:
                if not mst[end] and weight < key[end]:
                    key[end] = weight
                    heappush(q, [key[end], end])
    print('#{} {}'.format(test_case, result))