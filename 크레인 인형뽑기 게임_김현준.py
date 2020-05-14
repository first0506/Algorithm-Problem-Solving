def solution(board, moves):
    answer = 0
    box = []    # 바구니
    for j in moves:     # 크레인 위치 (열)
        j -= 1  # 인덱스 0부터 시작해서 -1
        for i in range(len(board)):
            if board[i][j]:     # 위에서부터 탐색, 인형 있으면
                if not box: # 바구니에 아무것도 없으면 그냥 넣기
                    box.append(board[i][j])
                else:
                    if box[-1]==board[i][j]:    # 바구니에 있는데 맨 위에거랑 같으면
                        box.pop()       # 빼기
                        answer += 2     # 2개 터트리기
                    else:
                        box.append(board[i][j]) # 같지 않으면 바구니에 넣기
                board[i][j] = 0 # 꺼낸 위치 0으로
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]    # 4
print(solution(board, moves))