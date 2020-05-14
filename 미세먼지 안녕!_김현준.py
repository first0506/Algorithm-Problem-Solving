di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def spread():   # 미세먼지 퍼짐
    arr1 = [[0]*C for _ in range(R)]    #또다른 배열 하나 생성
    for i in freshair:
        arr1[i[0]][i[1]] = -1       # 공기청정기 표시
    for i in range(R):
        for j in range(C):
            if arr[i][j] and arr[i][j]!=-1:     # 미세먼지 칸만 골라
                cnt = 0     # 4방향 중 퍼뜨릴 수 있는 방향 개수
                for d in range(4):
                    ni, nj = i+di[d], j+dj[d]
                    if 0<=ni<R and 0<=nj<C and arr[ni][nj] != -1:
                        cnt += 1
                        arr1[ni][nj] += arr[i][j]//5        # 생성한 배열에 더해준다.
                arr1[i][j] += arr[i][j]-(arr[i][j]//5)*cnt
    return arr1

def move():
    for i in range(2):      # 위쪽, 아래쪽 공기청정기
        a, b = freshair[i]      # 청정기 위치
        d = 0       # 출발 방향
        while 1:
            if i==0:
                ni = a+di[d]        # 위쪽이냐 아래쪽이냐에 따라 방향 바뀌는 순서가 다르다.(이 때 방향은 공기청정기 순환 반대방향)
            else:
                ni = a-di[d]
            nj = b+dj[d]
            if 0<=ni<R and 0<=nj<C:     # 벽에 만나지 않을 때
                if arr[a][b] != -1:     # 공기청정기에서 처음 시작할 떄가 아닐 때
                    arr[a][b] = arr[ni][nj]     # 앞의 미세먼지를 땡겨온다.
                arr[ni][nj] = 0     # 앞의 미세먼지는 0
                a, b = ni, nj
            else:
                d += 1  # 벽에 만나면 방향 바꾼다.
            if [a, b] == [freshair[i][0], C-1]:     # 마지막 진행 방향을 바꾸기 위한 조건
                d += 1
            if [a, b] == [freshair[i][0], 1]:   # 진행을 모두 마쳤을 때 조건
                break
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
freshair = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            freshair.append([i, j])
for _ in range(T):  # T번만큼 퍼뜨리기, 이동 반복
    arr = spread()
    move()

ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] and arr[i][j]!=-1: # 미세먼지 합 구하기
            ans += arr[i][j]
print(ans)