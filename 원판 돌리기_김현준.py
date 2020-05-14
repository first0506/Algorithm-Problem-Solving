di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def erase(i, j):
    v = [[0]*M for _ in range(N)]
    j = (j+pointers[i])%M   # 돌린 결과에 따른 좌표
    v[i][j] = 1
    queue = [[i, j, 1]]
    while queue:
        a, b, cnt = queue.pop(0)
        for d in range(4):
            ni = a+di[d]
            if 0<= ni <N:
                nj = (b+dj[d]-pointers[a]+pointers[ni])%M   # 이동 전 원판의 돌린 결과만큼 포인터를 뺴주고, 이동 후 원판의 돌린 결과 만큼 포인터를 더해준다.
                if 0<= nj <M and not v[ni][nj] and arr[a][b] == arr[ni][nj]:
                    v[ni][nj] = 1
                    queue.append([ni, nj, cnt+1])
    if cnt >= 2:    # 두 개 이상 이어지면
        for m in range(N):
            for n in range(M):
                if v[m][n] == 1:    # 이어진 곳의 숫자 모두 지우기
                    arr[m][n] = 0
        return True

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
pointers = [0]*N    # 맨 위쪽을 나타내는 인덱스 포인터
for _ in range(T):
    x, d, k = map(int, input().split())
    for i in range(N):
        if (i+1)%x == 0:    # 원판이 x의 배수일 때
            if d == 0:
                pointers[i] = (pointers[i]-k)%M     # 방향에 따른 포인터 이동
            else:
                pointers[i] = (pointers[i]+k)%M
    flag = False
    for i in range(N):
        for j in range(M):
            if arr[i][(j+pointers[i])%M]:   # 원판에 숫자가 지워지지 않았으면
                if erase(i, j): # 지우기 실행
                    flag = True
    if not flag:    # 지울 게 없을 때
        total, count = 0, 0
        for i in arr:
            for j in i:
                if j:   # 모든 지워지지 않은 숫자의 합과 개수를 구한다.
                    total += j
                    count += 1
        if count:   # 지워지지 않은 숫자가 있으면
            aver = total/count
            for i in range(N):
                for j in range(M):
                    if arr[i][j]:   # 각 숫자들을 조건에 따라 덧셈, 뺄셈
                        if arr[i][j] > aver:
                            arr[i][j] -= 1
                        elif arr[i][j] < aver:
                            arr[i][j] += 1
ans = 0
for m in range(N):
    for n in range(M):
        ans += arr[m][n]    # 지워지지 않은 모든 숫자의 합
print(ans)