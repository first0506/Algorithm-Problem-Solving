T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 2**31-1
    for i in range(1<<N):
        A = []
        for j in range(N):
            if i & (1<<j):
                A.append(h[j])
        if sum(A) >= B and sum(A)-B < ans:
            ans = sum(A)-B
        if ans == 0:
            break
    print('#{} {}'.format(test_case, ans))

from itertools import combinations
T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 2**31-1
    for k in range(1, N+1):
        tmp = combinations(h, k)
        for i in tmp:
            s = sum(i)
            if s>=B and s-B<ans:
                ans = s-B
            if not ans:
                break
        if not ans:
            break
    print('#{} {}'.format(test_case, ans))