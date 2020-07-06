import copy
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

# dfs(상어 x좌표, 상어 y좌표, 상어 이동방향, 임시 먹은 양, 공간, 물고기 정보)
def dfs(si, sj, sd, tmp, arr, fish):
    global ans
    # 최대값 갱신
    if tmp > ans:
        ans = tmp
    # 번호가 작은 물고기부터
    for i in range(1, 17):
        # 현재 물고기 x, y 좌표 및 이동방향
        m, n, d = fish[i][1], fish[i][2], fish[i][0]
        # 물고기가 살아 있으면
        if arr[m][n]==i:
            # 8방향 탐색
            for _ in range(8):
                ni, nj = m+di[d], n+dj[d]
                # 공간 안이고 상어가 아니면
                if 0<=ni<4 and 0<=nj<4 and arr[ni][nj]!=17:
                    # 이동할 위치에 이미 물고기가 있으면 그 물고기의 위치 정보를 바꿔준다.
                    if arr[ni][nj]:
                        fish[arr[ni][nj]][1], fish[arr[ni][nj]][2] = m, n
                    # 현재 물고기 정보 갱신
                    fish[i] = [d, ni, nj]
                    # 위치 변경
                    arr[m][n], arr[ni][nj] = arr[ni][nj], arr[m][n]
                    break
                # 반시계 방향
                d = (d+1)%8
    # 상어가 이동할 수 있는 거리는 최대 거리는 3
    for dist in range(1, 4):
        ni, nj = si+di[sd]*dist, sj+dj[sd]*dist
        # 공간 안이고, 물고기가 있으면
        if 0<=ni<4 and 0<=nj<4 and arr[ni][nj]:
            # 먹을 물고기 번호
            f = arr[ni][nj]
            # 새로운 상어 이동방향
            nd = fish[f][0]
            arr[si][sj] = 0
            arr[ni][nj] = 17
            # deepcopy 주의
            dfs(ni, nj, nd, tmp+f, copy.deepcopy(arr), copy.deepcopy(fish))
            # 원상복귀
            arr[ni][nj] = f
            arr[si][sj] = 17
# 공간
arr = [[0]*4 for _ in range(4)]
# 물고기 번호별 정보 저장
fish = [[] for _ in range(17)]
for i in range(4):
    info = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = info[2*j]
        # [이동방향, x, y]
        fish[info[2*j]] = [info[2*j+1]-1, i, j]
# (0, 0) 물고기를 상어가 먹은 시점부터 시작
ans = arr[0][0]
sd = fish[arr[0][0]][0]
arr[0][0] = 17
dfs(0, 0, sd, ans, arr, fish)

print(ans)