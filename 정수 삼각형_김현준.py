n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
for i in range(1, n):
    board[i][0] += board[i-1][0]    # 삼각형의 왼쪽 변 아래로 내려가면서 더함
    board[i][i] += board[i-1][i-1]  # 삼각형의 오른쪽 변 아래로 내려가면서 더함
for i in range(2, n):
    for j in range(1, i):
        board[i][j] += max(board[i-1][j-1], board[i-1][j])  # 대각선 왼쪽 또는 오른쪽 중 큰 수를 더함
print(max(board[-1]))