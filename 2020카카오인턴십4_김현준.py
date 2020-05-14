def solution(board):
    answer = 2**31-1
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    N = len(board)
    v = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        board[i] = [1]+board[i]+[1]
    board = [[1]*(N+2)]+board+[[1]*(N+2)]
    v[1][1] = 1
    def f(i, j, cost, lastD):
        nonlocal answer
        if i==N and j==N:
            if cost < answer:
                answer = cost
        elif cost < answer:
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]
                if not board[ni][nj] and not v[ni][nj]:
                    v[ni][nj] = 1
                    if not lastD ^ (d//2):
                        f(ni, nj, cost+100, d//2)
                    else:
                        f(ni, nj, cost+600, d//2)
                    v[ni][nj] = 0
    if not board[1][2]:
        f(1, 2, 100, 1)
    if not board[2][1]:
        f(2, 1, 100, 0)
    return answer

# board = [[0,0,0],[0,0,0],[0,0,0]]
# # result = 900

# board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# # result = 3800

board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
# result = 2100

# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
# # result = 3200

print(solution(board))