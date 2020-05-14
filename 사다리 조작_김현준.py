def select(k, i, start):
    if k == i:
        return ladder()     # 가로선 추가 횟수만큼 순열을 모두 뽑았을 때 ladder로 간다.
    else:
        for m in range(start, (N-1)*H-(i-k)+1):     # 중복이 되지 않는 이중리스트 순열 뽑기
            if garo[m//(N-1)][m%(N-1)] == 0:        # 해당 가로선이 비었을 때
                if m%(N-1) == 0 and garo[m//(N-1)][1]==0:       # 가로선이 0번(맨왼쪽)이고 오른쪽에 위치한 가로선이 비었으면
                    garo[m//(N-1)][m%(N-1)] = 1                 # 가로선을 채우고, 재귀
                    if select(k+1, i, m+1):
                        return True
                    garo[m//(N-1)][m%(N-1)] = 0
                elif 0< m%(N-1) <N-2 and garo[m//(N-1)][m%(N-1)-1]==0 and garo[m//(N-1)][m%(N-1)+1]==0:     # 가로선이 중간쯤 있고, 양쪽에 위치한 가로선이 비었으면
                    garo[m//(N-1)][m%(N-1)] = 1
                    if select(k+1, i, m+1):
                        return True
                    garo[m//(N-1)][m%(N-1)] = 0
                elif m%(N-1) == N-2 and garo[m//(N-1)][N-3]==0:     # 가로선이 N-2번(맨오른쪽)이고 왼쪽에 위치한 가로선이 비었으면
                    garo[m//(N-1)][m%(N-1)] = 1
                    if select(k+1, i, m+1):
                        return True
                    garo[m//(N-1)][m%(N-1)] = 0

def ladder():       # 각 출발점이 자기 자신으로 돌아오는지 판단
    sero = list(range(N))
    for i in range(H):
        for j in range(N-1):
            if garo[i][j] == 1:     # 가로선이 있으면 그 떄의 j와 j의 오른쪽에 있는 좌표를 바꾼다.
                sero[j], sero[j+1] = sero[j+1], sero[j]
    for i in range(N):
        if sero[i] != i:        # 모든 출발점이 자기 자신인지 체크
            return False
    return True

N, M, H = map(int, input().split())
garo = [[0]*(N-1) for _ in range(H)]        # 모든 가로선들을 배열로 만든다. N-1 X H
for _ in range(M):
    a, b = map(int, input().split())
    garo[a-1][b-1] = 1
ans = -1
if N == 2:  # N이 2인 경우 답은 0아니면 1밖에 나오지 않는다.
    if ladder():
        ans = 0
    else:
        ans = 1
else:
    for n in range(4):  # 가로선 추가 횟수
        if select(0, n, 0): # (n번 중 몇번째 추가인지, 가로선 총 추가 횟수, 순열을 위한 인덱스 시작포인트)
            ans = n     # select 함수에서 True가 나오면 그 때의 n을 정답으로
            break
print(ans)