import copy
N = int(input())
# 보드
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 회전
def rotate(arr):
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[j][N-1-i] = arr[i][j]
    return tmp
#
def move(arr):
    # 위로 이동하기
    for j in range(N):
        for i in range(N-1):
            # 위에서부터 빈칸찾기
            if not arr[i][j]:
                # 찾은 빈칸 아래에 있는 블록찾기
                for k in range(i+1, N):
                    if arr[k][j]:
                        # 찾은 빈칸에 블록 옮기고, 블록자리는 빈칸으로
                        arr[i][j]=arr[k][j]
                        arr[k][j]=0
                        break
                # 빈칸 아래에 블록이 없으면 break
                else:
                    break
            # 블록 합치기
            if arr[i][j]:
                for k in range(i+1, N):
                    # 현재 블록 아래에서 같은 숫자의 블록이 있으면 합치고, 아래 블록은 빈칸으로
                    if arr[k][j]:
                        if arr[i][j]==arr[k][j]:
                            arr[i][j] *= 2
                            arr[k][j]=0
                        break
                # 합칠 블록이 없으면 break
                else:
                    break
    return arr

def dfs(n, arr):
    global ans
    # 최대 5번 이동했을 때 최대값 갱신
    if n==5:
       for i in range(N):
           for j in range(N):
               if ans < arr[i][j]:
                   ans = arr[i][j]
    else:
        # 4방향으로 이동하기
        for _ in range(4):
            # 이동(deepcopy 주의)
            tmp = move(copy.deepcopy(arr))
            dfs(n+1, tmp)
            # 회전
            arr = rotate(arr)

dfs(0, arr)
print(ans)