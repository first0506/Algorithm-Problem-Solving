di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def search(i1, j1, k1, result1):
    queue = [[i1, j1, k1, result1]]
    while queue:
        i, j, k, result = queue.pop(0)
        if k == 6:
            if result not in v:
                v.append(result)
        else:
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]
                if 0<= ni <4 and 0<= nj <4:
                    queue.append([ni, nj, k+1, result+10**(k+1)*arr[ni][nj]])

T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    v = []
    for i in range(4):
        for j in range(4):
            search(i, j, 0, arr[i][j])
    print('#{} {}'.format(test_case, len(v)))

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def search(i, j, k, result):
    if k == 6:
        if result not in v:
            v.append(result)
    else:
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if 0<= ni <4 and 0<= nj <4:
                search(ni, nj, k+1, result+10**(k+1)*arr[ni][nj])

T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    v = []
    for i in range(4):
        for j in range(4):
            search(i, j, 0, arr[i][j])
    print('#{} {}'.format(test_case, len(v)))