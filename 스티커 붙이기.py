def check(i, j):
    for k in info:
        if 0<=i+k[0]<N and 0<=j+k[1]<M and arr[i+k[0]][j+k[1]]==0:
            pass
        else:
            return False
    for k in info:
        arr[i+k[0]][j+k[1]] = 1
    return True

def rotate(sticker):
    newsticker = [[0]*len(sticker) for _ in range(len(sticker[0]))]
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            newsticker[j][len(sticker)-i-1] = sticker[i][j]
    return newsticker

N, M, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(a)]
    flag = False
    for _ in range(4):
        info = []
        for i in range(a):
            for j in range(b):
                if sticker[i][j]==1:
                    m, n = i, j
                    break
            if sticker[i][j] == 1:
                break
        for i in range(a):
            for j in range(b):
                if sticker[i][j]==1:
                    info.append([i-m, j-n])
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    if check(i, j):
                        flag = True
                        break
            if flag:
                break
        if flag:
            break
        sticker = rotate(sticker)
        a, b = b, a

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            ans += 1
print(ans)