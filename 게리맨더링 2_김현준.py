def vote(i, j, d1, d2):
    global ans
    bound = [[0]*(N+1) for _ in range(N+1)] # 경계를 나타낼 수 있도록 배열을 하나 만든다.
    section1=section2=section3=section4=0
    for m in range(d1+1):       # 문제에 나와있는 경계선 조건을 통해 bound 안 경계선 위치에 1을 기록
        bound[i+m][j-m] = 1
    for m in range(d2+1):
        bound[i+m][j+m] = 1
    for m in range(d2+1):
        bound[i+d1+m][j-d1+m] = 1
    for m in range(d1+1):
        bound[i+d2+m][j+d2-m] = 1

    for m in range(i+d1):   # 문제에 나와있는 1번 선거구 조건을 이용한다. (이때 왼쪽부터 탐색하면서 경계선을 만나면 행을 바꾼다.)
        for n in range(1, j+1):
            if bound[m][n]:
                break
            else:
                section1 += arr[m][n]
    for m in range(1, i+d2+1):  # 2번 선거구 조건을 이용한다. (이때는 오른쪽부터 탐색하면서 경계선을 만나면 행을 바꾼다.)
        for n in range(N, j, -1):
            if bound[m][n]:
                break
            else:
                section2 += arr[m][n]
    for m in range(i+d1, N+1):
        for n in range(1, j-d1+d2):
            if bound[m][n]:
                break
            else:
                section3 += arr[m][n]
    for m in range(i+d2+1, N+1):
        for n in range(N, j-d1+d2-1, -1):
            if bound[m][n]:
                break
            else:
                section4 += arr[m][n]
    section5 = total-(section1+section2+section3+section4)  # 1~4번 선거구를 먼저 구한 뒤 전체에서 빼서 5번 선거구를 구한다.
    result = max(section1, section2, section3, section4, section5) - min(section1, section2, section3, section4, section5)
    if result < ans:
        ans = result

N = int(input())
arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)] # 인덱스 맞추기 위해 앞에 0을 더한다.
total = 0
ans = 2**31-1
for i in range(1, N+1):
    for j in range(1, N+1):
        total += arr[i][j]  # 전체 인구수를 구한다.
for i in range(1, N+1):
    for j in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if i+d1+d2 <=N and 1<= j-d1 < j < j+d2 <=N: # 문제에 나와있는 기준점, 경계의 길이 조건을 이용해 i,j,d1,d2를 찾는다.
                    vote(i, j, d1, d2)
print(ans)