def perm(i, used, result):
    global ans
    if i == N:
        if result > ans:
            ans = result
    else:
        for m in range(N):
            if not used[m] and result*(arr[i][m]/100) > ans:
                used[m] = 1
                perm(i+1, used, result*(arr[i][m]/100))
                used[m] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    used = [0]*N
    perm(0, used, 1)
    print('#{} {:.6f}'.format(test_case, ans*100))