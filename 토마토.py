from collections import deque
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(ik):
    global cnt
    queue = deque()
    v = [[0]*M for _ in range(N)]
    for i in ik:
        queue.append(i)
        v[i[0]][i[1]] = 1
    while queue:
        i, j, day = queue.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if 0<=ni<N and 0<=nj<M and not arr[ni][nj] and not v[ni][nj]:
                cnt -= 1
                if not cnt:
                    return day+1
                arr[ni][nj]=1
                v[ni][nj]=1
                queue.append([ni, nj, day+1])
    return -1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
ik = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            ik.append([i, j, 0])
        elif arr[i][j]==0:
            cnt += 1
if not cnt:
    print(0)
else:
    print(bfs(ik))