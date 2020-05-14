di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
types = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 1], [1, 2], [2, 3], [0, 3]]
possible = [[1, 2, 5, 6], [1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5]]
def escape(r1, c1):
    global ans
    queue = [[r1, c1, 1]]
    v[r1][c1] = 1
    while queue:
        r, c, t = queue.pop(0)
        if t >= L:
            break
        else:
            for d in types[arr[r][c]]:
                ni, nj = r+di[d], c+dj[d]
                if 0<= ni <N and 0<= nj <M and v[ni][nj] == 0 and arr[ni][nj] in possible[d]:
                    queue.append([ni, nj, t+1])
                    v[ni][nj] = 1
                    ans += 1

T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*M for _ in range(N)]
    ans = 1
    escape(R, C)
    print('#{} {}'.format(test_case, ans))