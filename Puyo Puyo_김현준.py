di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def bomb(i, j):
    v = [[0]*6 for _ in range(12)]
    v[i][j] = 1
    cnt = 1     # 연속된 뿌요 개수
    queue = [[i, j]]
    while queue:
        a, b = queue.pop(0)
        for d in range(4):
            ni, nj = a+di[d], b+dj[d]
            if 0<= ni <12 and 0<= nj <6 and not v[ni][nj] and arr[a][b] == arr[ni][nj]:
                v[ni][nj] = 1
                cnt += 1
                queue.append([ni, nj])
    if cnt >= 4:    # 4개이상 이어졌으면
        for m in range(12):
            for n in range(6):
                if v[m][n] == 1:
                    arr[m][n] = '.' #터뜨리기
        return True

def down():
    for j in range(6):  # 2048식 아래로 내리기
        for i in range(11, 0, -1):
            if arr[i][j] == '.':
                for k in range(i-1, -1, -1):
                    if arr[k][j] != '.':
                        arr[i][j], arr[k][j] = arr[k][j], arr[i][j]
                        break

arr = [list(input()) for _ in range(12)]
ans = 0
while 1:
    flag = False
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':    # 빈 곳이 아니면 터질 수 있는지 확인
                if bomb(i, j):
                    flag = True
    if flag:
        down()  # 터졌으면 아래로 내리기
        ans += 1    #연쇄+1
    else:
        break
print(ans)