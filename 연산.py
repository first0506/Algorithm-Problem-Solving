from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    v = [0]*1000001
    q = deque([[N, 0]])
    while q:
        n, i = q.popleft()
        if n==M:
            break
        if n<1000000 and not v[n+1]:
            v[n+1]=1
            q.append([n+1, i+1])
        if n>1 and not v[n-1]:
            v[n-1]=1
            q.append([n-1, i+1])
        if n<=500000 and not v[n*2]:
            v[n*2]=1
            q.append([n*2, i+1])
        if n>10 and not v[n-10]:
            v[n-10]=1
            q.append([n-10, i+1])
    print('#{} {}'.format(test_case, i))