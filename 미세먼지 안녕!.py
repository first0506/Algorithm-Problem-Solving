def spread():
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    arr1 = [[0]*C for _ in range(R)]
    arr1[fresh[0]][0], arr1[fresh[1]][0] = -1, -1
    for i in range(R):
        for j in range(C):
            if 0< arr[i][j] <5:
                arr1[i][j] += arr[i][j]
            elif arr[i][j] >= 5:
                cnt = 0
                a = []
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0<= ni <R and 0<= nj <C and arr[ni][nj] != -1:
                        cnt += 1
                        a.append([ni, nj])
                arr1[i][j] += arr[i][j] - (arr[i][j]//5) * cnt
                for m in a:
                    arr1[m[0]][m[1]] += arr[i][j]//5
    return arr1

def fan():
    arr[fresh[0]-1][0] = 0
    for i in range(fresh[0]-2, -1, -1):
        arr[i+1][0] = arr[i][0]
        arr[i][0] = 0
    for i in range(1, C):
        arr[0][i-1] = arr[0][i]
        arr[0][i] = 0
    for i in range(1, fresh[0]+1):
        arr[i-1][C-1] = arr[i][C-1]
        arr[i][C-1] = 0
    for i in range(C-2, 0, -1):
        arr[fresh[0]][i+1] = arr[fresh[0]][i]
        arr[fresh[0]][i] = 0

    arr[fresh[1]+1][0] = 0
    for i in range(fresh[1]+2, R):
        arr[i-1][0] = arr[i][0]
        arr[i][0] = 0
    for i in range(1, C):
        arr[R-1][i-1] = arr[R-1][i]
        arr[R-1][i] = 0
    for i in range(R-2, fresh[1]-1, -1):
        arr[i+1][C-1] = arr[i][C-1]
        arr[i][C-1] = 0
    for i in range(C-2, 0, -1):
        arr[fresh[1]][i+1] = arr[fresh[1]][i]
        arr[fresh[1]][i] = 0

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
fresh = []
for i in range(R):
    if arr[i][0] == -1:
          fresh.append(i)
for _ in range(T):
    arr = spread()
    fan()
ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            ans += arr[i][j]
print(ans)