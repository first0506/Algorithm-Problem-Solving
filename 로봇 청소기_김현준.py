di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def clean(r1, c1, d1):      #(처음 청소기 위치, 방향)
    r, c, d = r1, c1, d1
    arr[r][c] = 2       #  처음 위치 청소(2로 바꿈)
    cnt = 1             # 청소 횟수
    while 1:
        for i in range(1, 5):
            ni, nj, nd = r+di[(d-i)%4], c+dj[(d-i)%4], (d-i)%4      # 청소기 방향을 중심으로 시계 반대방향으로 탐색
            if 0<= ni <N and 0<= nj <M and arr[ni][nj] == 0:
                r, c, d = ni, nj, nd
                arr[r][c] = 2
                cnt += 1
                break
        else:
            ni, nj = r+di[(d+2)%4], c+dj[(d+2)%4]       # 청소 불가능 시 뒤로 이동
            if 0<= ni <N and 0<= nj <M and arr[ni][nj] != 1:
                r, c, d = ni, nj, d
            else:
                break
    return cnt

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(clean(r, c, d))