def solution(m, n, board):
    answer = 0
    board1 = [[] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            board1[i].append(board[i][j])
    while 1:
        v = [[0]*n for _ in range(m)]   # 방문 check
        for i in range(m-1):
            for j in range(n-1):
                if '.'!=board1[i][j]==board1[i+1][j]==board1[i][j+1]==board1[i+1][j+1]: # 2x2 사각형 존재 여부
                    v[i][j] = 1
                    v[i+1][j] = 1
                    v[i][j+1] = 1
                    v[i+1][j+1] = 1
        result = 0
        for i in range(m):
            for j in range(n):
                if v[i][j]: # 위에서 방문했으면 빈칸으로 만들고 result 증가
                    result += 1
                    board1[i][j] = '.'
        if not result:  # 사각형이 존재하지 않으면 break
            break
        else:
            answer += result    # 사각형 존재하면 result를 answer에 더함
        for j in range(n):
            for i in range(m-1, 0, -1):     # 블록 아래로 떨어트리기
                if board1[i][j] == '.':
                    for k in range(i-1, -1, -1):
                        if board1[k][j]!='.':
                            board1[i][j], board1[k][j] = board1[k][j], board1[i][j]
                            break
                    else:
                        break
    return answer

print(solution(4, 5, 	['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))