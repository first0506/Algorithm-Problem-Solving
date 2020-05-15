from heapq import heappush, heappop
V, E = map(int, input().split())
start = int(input())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
v = [2**31-1]*(V+1)
v[start] = 0
q = []
heappush(q, [0, start])
while q:
    w, s = heappop(q)
    for end, weight in arr[s]:
        weight += w
        if v[end] > weight:
            v[end] = weight
            heappush(q, [v[end], end])
for i in range(1, V+1):
    if v[i] < 2**31-1:
        print(v[i])
    else:
        print('INF')