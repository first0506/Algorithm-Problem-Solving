from collections import deque
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, list(input()))) for _ in range(N)]
#     v = [[2**31-1]*N for _ in range(N)]
#     v[0][0] = 0
#     q = deque([[0, 0, 0]])
#     while q:
#         i, j, time = deque.popleft(q)
#         for d in range(4):
#             ni, nj = i+di[d], j+dj[d]
#             if 0<=ni<N and 0<=nj<N and time+arr[ni][nj] < v[ni][nj]:
#                 v[ni][nj] = time+arr[ni][nj]
#                 q.append([ni, nj, v[ni][nj]])
#     print('#{} {}'.format(test_case, v[N-1][N-1]))

from heapq import heappush, heappop
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    v = [[2**31-1]*N for _ in range(N)]
    v[0][0] = 0
    q = []
    heappush(q, [0, 0, 0])
    while q:
        time, i, j= heappop(q)
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if 0<=ni<N and 0<=nj<N:
                tmp = time + arr[ni][nj]
                if tmp < v[ni][nj]:
                    v[ni][nj] = tmp
                    heappush(q, [tmp, ni, nj])
    print('#{} {}'.format(test_case, v[N-1][N-1]))