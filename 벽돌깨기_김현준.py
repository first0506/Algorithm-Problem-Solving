def c(choice, cnt): # 중복해서 뽑기(재귀)
    global min_left
    if cnt == N: # N개 모두 뽑았을 때
        arr2 = [[0]*W for _ in range(H)]
        for m in range(H):
            for n in range(W):
                arr2[m][n] = arr[m][n] # 원래 벽돌 배치 복사
        for k in choice:
            arr2 = bomb(k, arr2)    #폭탄 투하
        left = 0
        for m in range(H):
            for n in range(W):
                if arr2[m][n]:
                    left += 1 # 남은 벽돌 세기
        if left < min_left:
            min_left = left
    else:
        for j in range(W):
            choice[cnt] = j
            c(choice, cnt+1)
            if min_left == 0: # 남은 벽돌이 0개면 바로 스톱 (시간 save!!!!!!!!!!!)
                return

def bomb(k, arr2): # bfs를 이용한 벽돌 깨기
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    queue = []
    for h in range(H):
        if arr2[h][k]:
            queue.append([h, k]) #폭탄 투하시 가장 먼저 만나는 벽돌 찾기
            break
    while queue:
        a, b = queue.pop(0)
        power = arr2[a][b]
        arr2[a][b] = 0 # 벽돌 뿌시기
        for dir in range(4):
            a1, b1 = a, b
            pow_cnt = 1
            while pow_cnt < power: #벽돌의 파워 만큼 4방향으로 진행
                a1 += di[dir]
                b1 += dj[dir]
                if 0<= a1 <H and 0<= b1 <W:
                    if arr2[a1][b1] == 1: #크기가 1인 벽돌은 바로 깨버리기
                        arr2[a1][b1] = 0
                    else:
                        if arr2[a1][b1] > 1 and [a1, b1] not in queue: #크기가 2이상은 queue에 저장
                            queue.append([a1, b1])
                else:
                    break
                pow_cnt += 1
    down(arr2)
    return arr2

def down(arr2): # 깬 후 남은 벽돌 내리기
    for j in range(W):
        for i in range(H-1, 0, -1): # 각 열 중 큰 행부터 시작해서 처음 만난 0과 후에 만나는 0이 아닌 벽돌 교환
            if arr2[i][j] == 0:
                for k in range(i-1, -1, -1):
                    if arr2[k][j]:
                        arr2[i][j], arr2[k][j] = arr2[k][j], arr2[i][j]
                        break

T = int(input())
for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    choice = [0] * N # 떨어트릴 j좌표 위치 리스트
    min_left = 2**31-1
    c(choice, 0)
    print('#{} {}'.format(test_case, min_left))