def spread(arr):
    global ans
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    arrcopy = [[0] * M for _ in range(N)]
    for m in range(N):
        for n in range(M):
            arrcopy[m][n] = arr[m][n] # 연구소 복사
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2: # 입력으로 들어온 연구소의 바이러스만 체크하기
                queue = [[i, j]]
                while queue:
                    a, b = queue.pop(0)
                    for d in range(4):
                        ni = a + di[d]
                        nj = b + dj[d]
                        if 0<= ni <N and 0<= nj <M and arrcopy[ni][nj] == 0:
                            queue.append([ni, nj])
                            arrcopy[ni][nj] = 2 # 복사한 연구소에 바이러스 추가하기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arrcopy[i][j] == 0: # 안전 구역 세기
                cnt += 1
    if cnt > ans:
        ans = cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N*M-2): # 3개의 벽 고르기 (이중 리스트에 번호를 매겨 사용 0 ~ N*M-1)
    if arr[i // M][i % M] == 0: # 첫번쨰 벽
        for j in range(i+1, N*M-1):
            if arr[j // M][j % M] == 0: # 두번쨰 벽
                for k in range(j+1, N*M):
                    if arr[k // M][k % M] == 0: # 세번쨰 벽
                        arrcopy = [[0] * M for _ in range(N)] # 원래 연구소 복사 후 고른 벽 추가하기
                        for m in range(N):
                            for n in range(M):
                                arrcopy[m][n] = arr[m][n]
                        arrcopy[i // M][i % M] = 1
                        arrcopy[j // M][j % M] = 1
                        arrcopy[k // M][k % M] = 1
                        spread(arrcopy) # 바이러스 퍼지기
print(ans)