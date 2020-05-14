di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
Alp = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
def bfs():
    v = [0]*26
    v[Alp[arr[0][0]]] = 1
    queue = [[0, 0, 1, v]]
    while queue:
        i, j, length, v = queue.pop(0)
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            visit = v[:]
            if 0<=ni<R and 0<=nj<C and not visit[Alp[arr[ni][nj]]]:
                visit[Alp[arr[ni][nj]]] = 1
                queue.append([ni, nj, length+1, visit])
    print(length)

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
bfs()