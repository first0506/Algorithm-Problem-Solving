def combi(k, start, v):
    if k == M:
        cal(v)  # 조합 완료됐을 때 치킨 거리 구하기
    else:
        for i in range(start, len(chicken)-M+k+1):
            v[k] = i
            combi(k+1, i+1, v)

def cal(v):
    global ans
    result = 0
    for h in range(len(home)):  # 각 집마다 최소 거리를 구하고 이를 모두 더한다.
        min_din = 2**31-1
        for i in v:
            if length[h][i] < min_din:
                min_din = length[h][i]
        result += min_din
    if result < ans:    # 모두 더한 값과 ans를 비교
        ans = result

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
home = []       #집 위치 저장
chicken = []    # 치킨집 위치 저장
ans = 2**31-1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])
length = [[0]*len(chicken) for _ in range(len(home))]   # 각 집마다 모든 치킨집의 거리를 배열로 저장
for i in range(len(home)):
    for j in range(len(chicken)):
        length[i][j] = abs(home[i][0]-chicken[j][0]) + abs(home[i][1]-chicken[j][1])
combi(0, 0, [0]*M)  # 조합 시행
print(ans)