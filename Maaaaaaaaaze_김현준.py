dk = [-1, 1, 0, 0, 0, 0]
di = [0, 0, -1, 0, 1, 0]        # 3차원 탐색을 위한 6방향
dj = [0, 0, 0, 1, 0, -1]

def rotate(arr):    # 오른쪽으로 90도 회전하기
    arr1 = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            arr1[j][4-i] = arr[i][j]
    return arr1

def perm(k, used, order):   # 판의 쌓는 순서 순열
    if k == 5:
        if perm1(0, order, [0]*5):      # 쌓는 순서 다 고르면 돌리는 횟수
            return True
    else:
        for i in range(5):
            if not used[i]:
                used[i] = 1
                order[k] = i
                if perm(k+1, used, order):
                    return True
                used[i] = 0

def perm1(k, order, Rorder):    # 판 별 돌리는 횟수
    if k == 5:
        bfs(order, Rorder)  # 다 찾았으면 최단거리 찾기
        if ans == 12:   # 최소는 무조건 12이기 때문에 ans가 12이면 모든 과정 바로 종료
            return True
    elif k == 0:    # 처음에 (0, 0)에서 출발할 수 있는 돌리는 횟수 찾기
        for i in range(4):
            if arr[order[0]][i][0][0] == 1:
                Rorder[0] = i
                if perm1(1, order, Rorder):
                    return True
    elif k == 4:    # 마지막에 (4, 4)에서 도착할 수 있는 도릴는 횟수 찾기
        for i in range(4):
            if arr[order[4]][i][4][4] == 1:
                Rorder[4] = i
                if perm1(5, order, Rorder):
                    return True
    else:
        for i in range(4):
            Rorder[k] = i
            if perm1(k+1, order, Rorder):
                return True

def bfs(order, Rorder):
    global ans
    v = [[[0]*5 for _ in range(5)] for _ in range(5)]
    v[0][0][0] = 1  # visit 저장
    queue = [[0, 0, 0, 0]]  # [판, i, j 좌표, 이동횟수]
    while queue:
        k, i, j, length= queue.pop(0)
        if [k, i, j] == [4, 4, 4]:  #마지막에 도착했을 때 break
            if length < ans:
                ans = length
            break
        elif length >= ans: # 중간에 ans보다 이동횟수가 많아질 때 break
            break
        else:
            for d in range(6):  # 3차원으로 6방향에 대해 bfs실시
                nk, ni, nj = k+dk[d], i+di[d], j+dj[d]
                if 0<= nk <5 and 0<= ni <5 and 0<= nj <5 and not v[nk][ni][nj] and arr[order[nk]][Rorder[nk]][ni][nj] == 1:
                    v[nk][ni][nj] = 1
                    queue.append([nk, ni, nj, length+1])

arr = []
for _ in range(5):
    arr1 = [[list(map(int, input().split())) for _ in range(5)]]
    for _ in range(3):
        arr1.append(rotate(arr1[-1]))
    arr.append(arr1)
ans = 1000
perm(0, [0]*5, [0]*5)
if ans == 1000:
    ans = -1
print(ans)