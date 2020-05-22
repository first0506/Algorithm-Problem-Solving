from heapq import heappush, heappop
T = int(input())
for test_case in range(1, T+1):
    N, E = map(int, input().split())
    adj = {i:[] for i in range(N+1)}
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])
    v = [E*10]*(N+1)
    v[0] = 0
    q = []
    heappush(q, [0, 0])
    while q:
        w, s = heappop(q)
        for end, weight in adj[s]:
            weight += w
            if v[end] > weight:
                v[end] = weight
                heappush(q, [weight, end])
    print('#{} {}'.format(test_case, v[N]))