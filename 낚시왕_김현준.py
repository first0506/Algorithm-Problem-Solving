di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]
def move():
    arr1 = [[-1]*(C+2)]+[[-1]+[0]*C+[-1] for _ in range(R)]+[[-1]*(C+2)]    # 상어들이 움직인 후의 위치를 표현할 배열 생성
    for i in range(1, M+1):     # 1번 상어부터 탐색
        r, c, s, d, z = sharks[i]
        if arr[r][c] == i:      # 상어가 살아 있으면
            if d in [1, 2]:     # 이동방향이 '상하'면
                ns = s%((R-1)*2)    # (R-1)*2 시간마다 원래 위치로 되돌아오기 때문에 이를 이용해 나머지를 구한다.
                for _ in range(ns):     # ns 시간 움직임
                    if arr[r+di[d]][c] == -1:   # 벽에 닿으면
                        d = 3-d     #방향 반대로 바꿔준다.
                    r += di[d]      # 상어 이동
            else:
                ns = s%((C-1)*2)    # 이동방향이 '좌우'면
                for _ in range(ns):
                    if arr[r][c+dj[d]] == -1:
                        d = 7-d
                    c += dj[d]
            if not arr1[r][c]:      # 상어가 움직인 후의 위치에 다른 상어가 없으면
                arr1[r][c] = i      # 새로운 상어 위치에 상어 인덱스 표시
            else:       # 다른 상어가 이미 있으면
                if sharks[arr1[r][c]][4] < z:       # 이미 위치한 상어보다 크기가 더 크면
                    arr1[r][c] = i
            sharks[i] = [r, c, s, d, z]     # 최신 상어정보 업데이트
    return arr1     # 새로운 상어들의 배열을 return하여 최신화

R, C, M = map(int, input().split())
arr = [[-1]*(C+2)]+[[-1]+[0]*C+[-1] for _ in range(R)]+[[-1]*(C+2)]     # -1로 둘러싸인 배열
sharks = [[]]   # 상어 정보를 담은 배열 (인덱스1부터 시작하기 위해 빈 배열 추가)
ans = 0
for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    arr[r][c] = i       # 배열에 상어 위치에 상어 인덱스 표시
    sharks.append([r, c, s, d, z])      # [r, c, 속력, 이동방향, 크기]
for fishpoint in range(1, C+1):     # 낚시왕의 이동(좌->우)
    for row in range(1, R+1):
        if arr[row][fishpoint] > 0:     # 상어가 존재하면
            ans += sharks[arr[row][fishpoint]][4]   # 크기 더해주고 배열에 상어를 없애준다.
            arr[row][fishpoint] = 0
            break
    arr = move()    # 상어들의 움직임
print(ans)