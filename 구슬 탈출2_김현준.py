def down(arr):  # 2048 떄와 같이 아래로 구슬 이동
    global escape_flag
    for j in range(1, len(arr[0])-1):
        for i in range(len(arr)-2, 1, -1):
            if arr[i][j] == '.':    # 밑에서부터 첫번째 빈칸을 찾기
                for k in range(i-1, 0, -1):
                    if arr[k][j] == 'R' or arr[k][j] == 'B':    # 찾은 빈칸 이후로 구슬이 있으면
                        arr[i][j], arr[k][j] = arr[k][j], arr[i][j] # 위치 변경
                        break
                    elif arr[k][j] == 'O' and k != 1:   # 찾은 빈칸 이후로 구멍이 있고, 그 구멍이 1행에 없을 때
                        for m in range(k-1, 0, -1):
                            if arr[m][j] == 'R':    # 구멍 이후 빨간구슬 만났을 때 (파란구슬도 동시에 구멍에 빠질 수 있으므로 break 사용 X)
                                escape_flag = 1
                            elif arr[m][j] == 'B':  # 구멍 이후 파란구슬 만났을 때(break)
                                escape_flag = 2
                                break
                            elif arr[m][j] == '#':  # 구멍 이후 벽 만났을 때 (break)
                                break
                        break
                    elif arr[k][j] == '#':  # 찾은 빈칸 이후로 벽을 만났을 때
                        break
            elif arr[i][j] == 'O':  # 구슬만나기 전 구멍을 먼저 만나면
                for k in range(i-1, 0, -1):
                    if arr[k][j] == 'R':
                        escape_flag = 1
                    elif arr[k][j] == 'B':
                        escape_flag = 2
                        break
                    elif arr[k][j] == '#':
                        break
    return arr

def rotate(arr):    # 구슬판 회전 (가로 세로 길이가 다른 경우가 있으니 주의)
    arr1 = [[0]*len(arr) for _ in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr1[j][len(arr)-i-1] = arr[i][j]
    return arr1

def tilt(arr, cnt):
    global ans, escape_flag
    queue = []
    queue.append([arr, cnt])
    while queue:
        arr1, cnt1 = queue.pop(0)
        if cnt1 >= 11:  # 11번 이상 진행되면 바로 종료
            break
        else:
            flag = False
            for d in range(4):  # 4방향으로 기울이기
                escape_flag = 0 # 어떤 구슬이 구멍에 떨어졌는지 구분 (0: 안 떨어짐, 1: 빨간구슬, 2: 파란구슬)
                arr2 = [[0]*len(arr1[0]) for _ in range(len(arr1))]
                for i in range(len(arr2)):  # 구슬판 복사
                    for j in range(len(arr2[0])):
                        arr2[i][j] = arr1[i][j]
                if d != 0:  # 아래 방향을 제외한 나머지 방향을 위해 회전
                    for _ in range(d):
                        arr2 = rotate(arr2)
                arr2 = down(arr2)   # 아래 방향으로 기울이기
                if d != 0:  # 보기 편하게 다시 원래 방향으로 회전
                    for _ in range(4-d):
                        arr2 = rotate(arr2)
                if escape_flag == 1:    # 빨간 구슬만 빠졌으면 최소 횟수 저장
                    ans = cnt1
                    flag = True
                    break
                elif escape_flag == 0 and arr1 != arr2: # 구멍에 아무것도 빠지지 않고, 구슬의 위치가 바꼈을 때만 queue에 저장
                    queue.append([arr2, cnt1+1])
            if flag:
                break

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
escape_flag = 0
ans = -1
tilt(arr, 1)
print(ans)