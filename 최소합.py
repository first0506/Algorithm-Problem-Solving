T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        board[i][0] += board[i-1][0]
        board[0][i] += board[0][i-1]
    for i in range(1, N):
        for j in range(1, N):
            board[i][j] += min(board[i-1][j], board[i][j-1])
    print('#{} {}'.format(test_case, board[N-1][N-1]))