di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def combi(k, start, v):
    if k == M:
        spread(v, clean)
    else:
        for i in range(start, len(virus)-M+k+1):
            v[k] = i
            combi(k+1, i+1, v)

def spread(v, clean):
    global ans
    queue = []
    visit = [[0]*N for _ in range(N)]
    for i in v:
        a, b = virus[i]
        visit[a][b] = 1
        queue.append([a, b, 0])
    while queue:
        i, j, length = queue.pop(0)
        if length >= ans:
            break
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if 0<=ni<N and 0<=nj<N and not visit[ni][nj] and arr[ni][nj] != 1:
                if arr[ni][nj] == 0:
                    visit[ni][nj] = 1
                    clean -= 1
                    queue.append([ni, nj, length+1])
                elif arr[ni][nj] == 2:
                    if clean:
                        visit[ni][nj] = 1
                        queue.append([ni, nj, length+1])
    if not clean and length < ans:
        ans = length

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 2**31-1
virus = []
clean = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            clean += 1
        elif arr[i][j] == 2:
            virus.append([i, j])
combi(0, 0, [0]*M)
if ans == 2**31-1:
    ans = -1
print(ans)