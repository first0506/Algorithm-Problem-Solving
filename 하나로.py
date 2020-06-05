# from heapq import heappush, heappop
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     X = list(map(int, input().split()))
#     Y = list(map(int, input().split()))
#     E = float(input())
#     arr = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             arr[i][j] = (abs(X[i]-X[j])**2+abs(Y[i]-Y[j])**2)*E
#     ans = 0
#     v = [0]*N
#     costs = [float('inf')]*N
#     costs[0] = 0
#     q = []
#     heappush(q, [0, 0])
#     while q:
#         cost, i = heappop(q)
#         if not v[i]:
#             v[i] = 1
#             ans += cost
#         for k in range(N):
#             tmp = arr[i][k]
#             if not v[k] and costs[k]>tmp:
#                 costs[k] = tmp
#                 heappush(q, [tmp, k])
#     print('#{} {}'.format(test_case, round(ans)))

from heapq import heappush, heappop
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    ans = 0
    v = [0]*N
    costs = [float('inf')]*N
    costs[0] = 0
    q = []
    heappush(q, [0, 0])
    while q:
        cost, i = heappop(q)
        if not v[i]:
            v[i] = 1
            ans += cost
            for k in range(N):
                tmp = (abs(X[i]-X[k])**2+abs(Y[i]-Y[k])**2)*E
                if not v[k] and costs[k]>tmp:
                    costs[k] = tmp
                    heappush(q, [tmp, k])
    print('#{} {}'.format(test_case, round(ans)))