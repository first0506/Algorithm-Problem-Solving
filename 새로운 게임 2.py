di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]
def move():
    for num in range(1, K+1):
        i, j = horse[num][0], horse[num][1]
        ni, nj = i+di[horse[num][2]], j+dj[horse[num][2]]
        k = 0
        for m in range(len(arr1[i][j])):
            if arr1[i][j][m] == num:
                k = m
                break
        if arr[ni][nj] == 0:
            arr1[ni][nj] += arr1[i][j][k:]
            arr1[i][j] = arr1[i][j][:k]
        elif arr[ni][nj] == 1:
            a = []
            for m in range(len(arr1[i][j])-1, k-1, -1):
                a.append(arr1[i][j][m])
            arr1[ni][nj] += a
            arr1[i][j] = arr1[i][j][:k]
        elif arr[ni][nj] == 2:
            if horse[num][2] < 3:
                horse[num][2] = 3-horse[num][2]
            else:
                horse[num][2] = 7-horse[num][2]
            ni, nj = i+di[horse[num][2]], j+dj[horse[num][2]]
            if arr[ni][nj] == 0:
                arr1[ni][nj] += arr1[i][j][k:]
                arr1[i][j] = arr1[i][j][:k]
            elif arr[ni][nj] == 1:
                a = []
                for m in range(len(arr1[i][j])-1, k-1, -1):
                    a.append(arr1[i][j][m])
                arr1[ni][nj] += a
                arr1[i][j] = arr1[i][j][:k]
            elif arr[ni][nj] == 2:
                ni, nj = i, j
        for m in arr1[ni][nj]:
            horse[m][0], horse[m][1] = ni, nj
        if len(arr1[ni][nj]) >= 4:
            return True

N, K = map(int, input().split())
arr = [[2]*(N+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(N)]+[[2]*(N+2)]
arr1 = [[[] for _ in range(N+2)] for _ in range(N+2)]
horse = [[] for _ in range(K+1)]
for i in range(K):
    a, b, c = map(int, input().split())
    horse[i+1] = [a, b, c]
    arr1[a][b].append(i+1)
ans = -1
for i in range(1, 1001):
    if move():
        ans = i
        break
print(ans)