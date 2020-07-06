import pprint
def rotate(arr):
    arr1 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr1[j][N-1-i] = arr[i][j]
    return arr1

def combine(arr):
    for j in range(N):
        for i in range(N-1):
            if arr[i][j]:
                for k in range(i+1, N):
                    if arr[k][j]:
                        if arr[i][j] == arr[k][j]:
                            arr[i][j] *= 2
                            arr[k][j] = 0
                        break
    return arr

def up(arr):
    for j in range(N):
        for i in range(N-1):
            if not arr[i][j]:
                for k in range(i+1, N):
                    if arr[k][j]:
                        arr[i][j], arr[k][j] = arr[k][j], arr[i][j]
                        break
    return arr

def move(arr, k):
    global ans
    print(k)
    pprint.pprint(arr)
    if k == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > ans:
                    ans = arr[i][j]
    else:
        for d in range(4):
            arr1 = [[0]*N for _ in range(N)]
            for m in range(N):
                for n in range(N):
                    arr1[m][n] = arr[m][n]
            for _ in range(d):
                arr1 = rotate(arr1)
            arr1 = combine(arr1)
            arr1 = up(arr1)
            move(arr1, k+1)

N = int(input())
ans = 0
arr = [list(map(int, input().split())) for _ in range(N)]
move(arr, 0)
print(ans)