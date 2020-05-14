def f(n, tmp):
    global ans
    if n==(N+1):
        if tmp < ans:
            ans = tmp
    elif tmp < ans:
        for i in range(N):
            if i not in road or (not i and len(road)==N):
                tmp += board[road[-1]][i]
                road.append(i)
                f(n+1, tmp)
                road.pop()
                tmp -= board[road[-1]][i]
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 2**31-1
    road = [0]
    f(1, 0)
    print('#{} {}'.format(test_case, ans))