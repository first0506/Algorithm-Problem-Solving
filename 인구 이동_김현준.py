def bfs(i, j):
    global used
    uni = []
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    queue = []
    queue.append([i, j])
    used[i][j] = 1
    while queue:
        a, b = queue.pop(0)
        uni.append([a, b, arr[a][b]])
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0<= ni <N and 0<= nj <N and L<= abs(arr[a][b] - arr[ni][nj]) <=R and used[ni][nj] == 0:
                queue.append([ni, nj])
                used[ni][nj] = 1
    return uni

def bfs_possible(i, j):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    flag = False
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and L<= abs(arr[i][j] - arr[ni][nj]) <=R:
            flag = True
            break
    return flag

def move(uni):
    ppls = 0
    for i in uni:
        ppls += i[2]
    ppls = ppls//len(uni)
    for i in uni:
        arr[i[0]][i[1]] = ppls

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while 1:
    used = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if used[i][j] == 0 and bfs_possible(i, j):
                move(bfs(i, j))
                flag = True
    if flag:
        ans += 1
    else:
        break
print(ans)