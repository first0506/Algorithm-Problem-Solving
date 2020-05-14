def solution(board, moves):
    answer = 0
    stack = []
    for j in moves:
        crain = 0
        for i in range(len(board)):
            if board[i][j-1]:
                crain = board[i][j-1]
                board[i][j-1] = 0
                break
        if crain:
            if not stack:
                stack.append(crain)
            else:
                if crain == stack[-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(crain)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
result = solution(board, moves)
print(result)