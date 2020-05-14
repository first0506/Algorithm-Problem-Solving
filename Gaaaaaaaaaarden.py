import pprint
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def combi(k, num, g, r):
    if k == G+R:
        spread()
    else:
        for i in range(num, numb-(G+R)+k+1):
            for j in range(1, 3):
                if j==1 and g!=G:
                    usedbae[i]=1
                    combi(k+1, i+1, g+1, r)
                    usedbae[i]=0
                if j==2 and r!=R:
                    usedbae[i]=2
                    combi(k+1, i+1, g, r+1)
                    usedbae[i]=0

def spread():
    global ans
    land = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            land[i][j] = arr[i][j]
    queue = []
    for i in range(numb):
        if usedbae[i]==1:
            queue.append([1, bae[i], 3])
            land[bae[i][0]][bae[i][1]] = 3
        elif usedbae[i]==2:
            queue.append([2, bae[i], -3])
            land[bae[i][0]][bae[i][1]] = -3
    while queue:
        col, [m, n], time = queue.pop(0)
        if land[m][n]!='*':
            for d in range(4):
                ni, nj = m+di[d], n+dj[d]
                if 0<=ni<N and 0<=nj<M and land[ni][nj]!=0:
                    if land[ni][nj]==1 or land[ni][nj]==2:
                        if col==1:
                            land[ni][nj] = time+1
                            queue.append([1, [ni, nj], time+1])
                        else:
                            land[ni][nj] = time-1
                            queue.append([2, [ni, nj], time-1])
                    elif (col==1 and land[ni][nj]==-(time+1)) or (col==2 and land[ni][nj]==-(time-1)):
                        land[ni][nj] = '*'
    result = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] == '*':
                result += 1
    if result > ans:
        ans = result

N, M, G, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bae = []
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            bae.append([i, j])
numb = len(bae)
usedbae = [0]*numb
combi(0, 0, 0, 0)
print(ans)