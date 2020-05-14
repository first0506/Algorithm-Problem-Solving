def solution(board):
    answer = 0
    N = len(board)
    while 1:
        for j in range(N):
            flag = False
            for i in range(N):
                if board[i][j]:
                    if check1(i-1, j, board, N):
                        answer += 1
                        flag = True
                    break
            if flag:
                break
        if not flag:
            break
    return answer

def check1(i, j, board, N):
    if 0<j<(N-1) and board[i][j-1]==board[i+1][j-1]==board[i+1][j]==board[i+1][j+1] and check2(board, i, j+1):
        board[i][j-1]=board[i+1][j-1]=board[i+1][j]=board[i+1][j+1]=0
        return True
    elif j<(N-1) and board[i+1][j]==board[i+1][j+1]==board[i][j+1]==board[i-1][j+1]:
        board[i+1][j]=board[i+1][j+1]=board[i][j+1]=board[i-1][j+1]=0
        return True
    elif 0<j and board[i-1][j-1]==board[i][j-1]==board[i+1][j-1]==board[i+1][j]:
        board[i-1][j-1]=board[i][j-1]=board[i+1][j-1]=board[i+1][j]=0
        return True
    elif j<(N-2) and board[i+1][j]==board[i+1][j+1]==board[i+1][j+2]==board[i][j+2] and check2(board, i, j+1):
        board[i+1][j]=board[i+1][j+1]=board[i+1][j+2]=board[i][j+2]=0
        return True
    elif j<(N-2) and board[i+1][j]==board[i+1][j+1]==board[i][j+1]==board[i+1][j+2] and check2(board, i, j+2):
        board[i+1][j]=board[i+1][j+1]=board[i][j+1]=board[i+1][j+2]=0
        return True
    return False

def check2(board, i, j):
    for k in range(i+1):
        if board[k][j]:
            return False
    return True

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
# result = 2

print(solution(board))