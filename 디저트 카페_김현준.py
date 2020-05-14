def length(i, j):
    for m in range(1, min((N - 2) - i, (N - 1) - j) + 1):   # 각 투어 처음 위치에서 직선으로 최대한 갈 수 있는 길이 구하기 (오른쪽벽에 먼저 닿을지, 아래쪽 벽에 닿을지 둘 중 하나)
        for n in range(1, min((N - 1) - (i + m), j) + 1):   # 두 번쨰로 갈 수 있는 최대 길이 구하기 (아래쪽 벽에 닿을지, 왼쪽 벽에 닿을지)
            tour(m, n, i, j)    # for문으로 변의 길이를 1부터 최대길이 m, n까지 모든 경우의 수를 구한 것이다.


def tour(m, n, i, j):
    visited = [arr[i][j]]   # 카페의 숫자를 넣어가면서 중복된 숫자를 만나면 break한다.
    global ans
    flag = True
    for _ in range(m):  # 첫번쨰 직선 경로
        i += 1
        j += 1
        if arr[i][j] not in visited:
            visited.append(arr[i][j])
        else:
            flag = False
            break
    if flag:
        for _ in range(n):  # 두번쨰
            i += 1
            j -= 1
            if arr[i][j] not in visited:
                visited.append(arr[i][j])
            else:
                flag = False
                break
        if flag:
            for _ in range(m):  # 세번쨰
                i -= 1
                j -= 1
                if arr[i][j] not in visited:
                    visited.append(arr[i][j])
                else:
                    flag = False
                    break
            if flag:
                for _ in range(n - 1):  #4번쨰 (이떄는 출발점으로 되돌아가기 때문에 n반복이 아닌 n-1반복만 한다.
                    i -= 1
                    j += 1
                    if arr[i][j] not in visited:
                        visited.append(arr[i][j])
                    else:
                        flag = False
                        break
    if flag:    # 모든 경로를 다 돌았을 때
        if 2 * (m + n + 2) - 4 > ans:
            ans = 2 * (m + n + 2) - 4


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for i in range(N - 2):      # 카페 투어 가능한 처음 위치 설정
        for j in range(1, N - 1):
            length(i, j)
    print('#{} {}'.format(test_case, ans))