di=[-1, 0, 1, 0]
dj=[0, 1, 0, -1]

def bfs(sr, sc):
    queue = [[sr, sc, 0]]
    v = [[0]*(N+2) for _ in range(N+2)]
    v[sr][sc] = 1
    while queue:
        i, j, length = queue.pop(0)
        if arr[i][j]=='3':
            return length-1
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if arr[ni][nj]!='1' and not v[ni][nj]:
                queue.append([ni, nj, length+1])
                v[ni][nj] = 1
    return 0

T= int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [['1']*(N+2)] + [['1']+list(input())+['1'] for _ in range(N)] + [['1']*(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            if arr[i][j]=='2':
                sr, sc = i, j
    print('#{} {}'.format(test_case, bfs(sr, sc)))