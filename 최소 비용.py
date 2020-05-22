from heapq import heappush, heappop
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[N**2*1001]*N for _ in range(N)]
    v[0][0] = 0
    q = []
    heappush(q, [0, 0, 0])
    while q:
        w, i, j = heappop(q)
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if 0<=ni<N and 0<=nj<N:
                weight = w + 1
                if arr[ni][nj]>arr[i][j]:
                    weight += arr[ni][nj]-arr[i][j]
                if v[ni][nj] > weight:
                    v[ni][nj] = weight
                    heappush(q, [weight, ni, nj])
    print('#{} {}'.format(test_case, v[N-1][N-1]))