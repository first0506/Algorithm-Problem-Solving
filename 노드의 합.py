# def f(node):
#     global ans
#     if node*2 <= N:
#         f(node*2)
#     else:
#         ans += v[node]
#     if node*2+1 <= N:
#         f(node*2+1)
#
# T = int(input())
# for test_case in range(1, T+1):
#     N, M, L = map(int, input().split())
#     ans = 0
#     v = [0]*(N+1)
#     for _ in range(M):
#         a, b = map(int, input().split())
#         v[a] = b
#     f(L)
#     print('#{} {}'.format(test_case, ans))

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    ans = 0
    for _ in range(M):
        a, b = map(int, input().split())
        i = 1
        while 1:
            print(a>>i)
            if (a>>i)==L:
                ans += b
                break
            elif (a>>i)<L:
                break
            else:
                i += 1
    print('#{} {}'.format(test_case, ans))