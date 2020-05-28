def dfs(n):
    global ans
    if n==cnt:
        if ans < int(''.join(num)):
            ans = int(''.join(num))
    else:
        for i in range(N-1):
            for j in range(i+1, N):
                num[i], num[j] = num[j], num[i]
                tmp = int(''.join(num))
                if not tmp in v[n]:
                    v[n].append(tmp)
                    dfs(n+1)
                num[i], num[j] = num[j], num[i]

T = int(input())
for test_case in range(1, T+1):
    num, cnt = input().split()
    num = list(num)
    cnt = int(cnt)
    N = len(num)
    v = [[] for _ in range(cnt)]
    ans = 0
    dfs(0)
    print('#{} {}'.format(test_case, ans))