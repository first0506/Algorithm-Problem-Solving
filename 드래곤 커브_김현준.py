di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
dir = [1, 2, 3, 0]  # 90도 꺾었을 때 방향도 바뀌게 된다 그 때의 방향 모음
N = int(input())
arr = [[0]*101 for _ in range(101)] # 방문할 좌표를 찍을 arr
for _ in range(N):
    j, i, d, g = map(int, input().split())  # i와 j가 바뀌어 있음을 주의하자
    dirs = [d]  # dir = 출발부터 움직이는 모든 방향
    arr[i][j] = 1   # 처음 위치 표시
    for _ in range(g):
        change = [] # 회전했을 때 방향의 모음들
        for m in dirs[::-1]:    # 끝점을 중심으로 90도 회전하기 때문에 마지막 방향부터 바꿔준다
            change.append(dir[m])
        dirs = dirs + change    # 기존 방향들의 집합과 회전했을 때의 방향 집합을 더해준다.
    for m in dirs:
        i += di[m]
        j += dj[m]
        arr[i][j] = 1   #진행하면서 좌표에 표시
ans = 0
for m in range(100):
    for n in range(100):    #정사각형의 우상 좌표들
        if arr[m][n] and arr[m+1][n] and arr[m][n+1] and arr[m+1][n+1]: # 4꼭짓점에 모두 방문했으면
            ans += 1
print(ans)