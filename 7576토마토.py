def bfs(N, M):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = [0]*N*M # 큐 생성
    visited = [[0]*M for _ in range(N)] # visited생성
    front = -1
    rear = -1
    # 시작점 enq
    rare = 0
    done = 0
    for i in range(N):
        for j in range(M):
            if box[i][j]==1:
                rear += 1
                q[rear] = (i, j)
                visited[i][j] = 1
                done += 1
            elif box[i][j]==0:
                rare += 1
    if rare==0 and done!=0: # 익은토마토만 있는 경우
        return 0
    last = 0
    cnt = 0
    while front != rear:    # 큐가 비어있지 않으면
        front += 1
        i, j = q[front]
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<M and box[ni][nj]==0 and visited[ni][nj]==0:
                rear += 1
                q[rear] = (ni, nj)
                visited[ni][nj] = visited[i][j]+1
                last = visited[ni][nj]
                cnt += 1
    if rare != cnt: # 안익은 개수 != 익은 개수
        return -1
    else: # 다 익었으면
        return last - 1





M, N = map(int, input().split())
box = [list(map(int, input().split())) for i in range(N)]
print(bfs(N, M))