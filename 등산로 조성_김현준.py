di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def hiking(i, j, flag, val, level, v):      # (좌표, 공사 여부, 좌표에 해당하는 값, 등산로길이, visit여부)
    global ans
    v[i*N+j] = 1    # 처음 시작 위치 visit
    queue = [[i, j, flag, val, level, v]]
    while queue:
        a, b, flag1, val1, level1, v1 = queue.pop(0)    # (현재 위치, 공사 여부, 현재 높이, 등산로길이, visit여부)
        for d in range(4):
            ni, nj = a+di[d], b+dj[d]
            if 0<= ni <N and 0<= nj <N and not v1[ni*N+nj] and val1 > arr[ni][nj]:  # 공사가 필요없을 때
                v1[ni*N+nj] = 1
                queue.append([ni, nj, flag1, arr[ni][nj], level1+1, v1[:]])
                v1[ni*N+nj] = 0
            elif 0<= ni <N and 0<= nj <N and not v1[ni*N+nj] and not flag1 and arr[ni][nj] - (val1-1) <= K: # 공사가 필요 and 다음 위치의 높이를 현재 위치의 높이-1 로 공사할 수 있는지 여부 (현재 높이-1로 공사하는게 best)
                v1[ni*N+nj] = 1
                queue.append([ni, nj, True, val1-1, level1+1, v1[:]])   # 공사여부 flag를 True로, 공사를 진행했기 때문에 현재높이-1로 넘겨준다.
                v1[ni*N+nj] = 0
    if level1 > ans:    # 마지막 queue 원소의 level을 ans와 비교
        ans = level1

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start = 0
    start1 = []
    for i in range(N):
        for j in range(N):          # 가장 높은 높이와 위치찾기
            if arr[i][j] > start:
                start = arr[i][j]
                start1 = [[i, j]]
            elif arr[i][j] == start:
                start1.append([i, j])
    ans = 0
    for i in start1:
        a, b = i[0], i[1]
        v = [0]*(N**2)      # visit
        hiking(a, b, False, start, 1, v)
    print('#{} {}'.format(test_case, ans))