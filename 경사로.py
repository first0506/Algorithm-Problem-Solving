def rotate(arr):
    arr1 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr1[j][N-i-1] = arr[i][j]
    return arr1

def search():
    global ans
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            d = arr[i][j+1]-arr[i][j]
            if d == 1 and cnt >= L:
                cnt = 1
            elif d == 0:
                cnt += 1
            elif d == -1 and cnt >= 0:
                cnt = -L+1
            else:
                break
        else:
            if cnt >= 0:
                ans += 1

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
search()
arr = rotate(arr)
search()
print(ans)