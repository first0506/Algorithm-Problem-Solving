di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
# 2로 둘러싸인 보드 생성
arr = [[2]*(N+2) for _ in range(N+2)]
for i in range(1, N+1):
    for j in range(1, N+1):
        arr[i][j] = 0
# 사과 생성
K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    arr[i][j] = 1
# snake에 뱀 좌표 저장, 보드에 뱀의 위치 2로 표시
snake = [[1, 1]]
arr[1][1] = 2
d = 0
ans = 0
# 방향 변환 정보 저장
L = int(input())
infos = []
for _ in range(L):
    X, C = input().split()
    X = int(X)
    infos.append([X, C])

while 1:
    ans += 1
    # 뱀의 머리 새로운 위치 좌표
    ni, nj = snake[-1][0]+di[d], snake[-1][1]+dj[d]
    # 벽이거나 자기 몸과 만나면
    if arr[ni][nj]==2:
        break
    # 안 만났을 때 머리 추가
    snake.append([ni, nj])
    # 사과를 만나지 않으면 꼬리 떼고 0으로 초기화
    if not arr[ni][nj]:
        m, n = snake.pop(0)
        arr[m][n] = 0
    arr[ni][nj] = 2
    # 각 X초가 되면 방향 변환
    if infos and ans==infos[0][0]:
        if infos[0][1]=='L':
            d = (d-1)%4
        else:
            d = (d+1)%4
        infos.pop(0)

print(ans)