di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def search(i1, j1, n1):
    global maxCnt, Num
    i, j, n = i1, j1, n1
    cnt = 1
    while 1:
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<= ni <N and 0<= nj <N and arr[ni][nj] == n+1:
                i, j, n = ni, nj, n+1
                cnt += 1
                break
        else:
            break
    if cnt > maxCnt:
        maxCnt = cnt
        Num = arr[i1][j1]
    elif cnt == maxCnt:
        if arr[i1][j1] < Num:
            Num = arr[i1][j1]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Num = 0
    maxCnt = 0
    for i in range(N):
        for j in range(N):
            if N**2+1 - arr[i][j] > maxCnt or (N**2+1-arr[i][j] == maxCnt and arr[i][j] < Num):
                search(i, j, arr[i][j])
    print('#{} {} {}'.format(test_case, Num, maxCnt))

# 선생님 풀이
'''
cnt[N*N]부터 왼쪽으로 연속한 1의 개수를 확인해 가장 긴 구간을 찾는다.
연속한 개수가 같으면 더 왼쪽인 구간을 선택한다.
마지막 구간의 가장 왼쪽 인덱스와 구간의 길이+1을 출력한다.
'''
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*(N**2+1)
    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]
                if 0<= ni <N and 0<= nj <N and arr[ni][nj] == arr[i][j]+1:
                    v[arr[i][j]] = 1
                    break
    Num, maxCnt, length = 0, 0, 0
    for i in range(1, N**2+1):
        if v[i]:
            length += 1
        elif not v[i] and length:
            if maxCnt < length:
                maxCnt = length
                Num = i-length
            length = 0
    print('#{} {} {}'.format(test_case, Num, maxCnt+1))