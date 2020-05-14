def spr_sum():
    for i in range(1, N+1):
        for j in range(1, N+1):
            if tree[i][j]:

                newTree = []
                tree[i][j].sort()
                for m in range(len(tree[i][j])):
                    if tree[i][j][m] <= current[i][j]:
                        current[i][j] -= tree[i][j][m]
                        newTree.append(tree[i][j][m]+1)
                    else:
                        for n in range(m, len(tree[i][j])):
                            current[i][j] += (tree[i][j][n]//2)
                        break
                tree[i][j] = newTree

def fall():
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if tree[i][j]:
                for t in tree[i][j]:
                    if t%5 == 0:
                        for d in range(8):
                            ni, nj = i+di[d], j+dj[d]
                            if 1<=ni<=N and 1<=nj<=N:
                                tree[ni][nj].append(1)

def winter():
    for i in range(1, N+1):
        for j in range(1, N+1):
            current[i][j] += food[i][j]

N, M, K = map(int ,input().split())
current = [[0]*(N+2)]+[[0]+[5]*N+[0] for _ in range(N)]+[[0]*(N+2)]
food = [[0]*(N+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(N+2)]
tree = [[[] for _ in range(N+2)] for _ in range(N+2)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x][y].append(z)
ans = 0
for _ in range(K):
    spr_sum()
    fall()
    winter()
for i in range(1, N+1):
    for j in range(1, N+1):
        ans += len(tree[i][j])
print(ans)