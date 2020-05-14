def tilt(Rr, Rc, Br, Bc, cnt):
    global ans
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    queue = [[Rr, Rc, Br, Bc, cnt]]     # 구슬 좌표와 기울인 횟수
    while queue:
        firstR1, firstC1, secondR1, secondC1, count = queue.pop(0)      # 먼저 움직이는 구슬 좌표, 나중에 움직이는 구슬 좌표
        if count >= 11:     # 10회 초과면 break
            break
        flag = False
        for d in range(4):
            Redhole = Bluehole = False      # 구슬 색에 따라 구멍에 빠졌는지 알기 위한 flag
            if d == 0:
                if abs(firstR1) > abs(secondR1):
                    firstR1, firstC1, secondR1, secondC1 = secondR1, secondC1, firstR1, firstC1     # 두 구슬이 같은 행이나 열에 있을 때 기울이는 방향에 따라 먼저 움직여야 하는 구슬이 정해져 있으므로, 그것을 위해 어느 구슬을 먼저할 지 결정
            if d == 1:
                if abs(firstC1) < abs(secondC1):
                    firstR1, firstC1, secondR1, secondC1 = secondR1, secondC1, firstR1, firstC1
            if d == 2:
                if abs(firstR1) < abs(secondR1):
                    firstR1, firstC1, secondR1, secondC1 = secondR1, secondC1, firstR1, firstC1
            if d == 3:
                if abs(firstC1) > abs(secondC1):
                    firstR1, firstC1, secondR1, secondC1 = secondR1, secondC1, firstR1, firstC1
            firstR, firstC, secondR, secondC = firstR1, firstC1, secondR1, secondC1     # 나중에 시간을 단축하기 위한 if문을 위해 기울이기 전 좌표 저장
            while 1:
                if firstR > 0:      # 먼저 움직이는 구슬이 어떤 색인지 모르므로 색에 따라 바꿔준다.
                    firstR += di[d]
                    firstC += dj[d]
                else:
                    firstR -= di[d]
                    firstC -= dj[d]
                if arr[abs(firstR)][abs(firstC)] == 'O':    # 구멍을 만나면
                    if firstR > 0:
                        Redhole = True      # 좌표의 부호에 따라 색을 알 수 있기 떄문에 좌표에 따라 flag 값 변경
                    else:
                        Bluehole = True
                    break
                elif arr[abs(firstR)][abs(firstC)] == '#':      # 현재 좌표가 벽이면 벽의 좌표 바로 전 좌표로 돌아간다.
                    if firstR > 0 or firstC > 0:
                        firstR -= di[d]
                        firstC -= dj[d]
                    elif firstR < 0 or firstC < 0:
                        firstR += di[d]
                        firstC += dj[d]
                    break

            while 1:
                if secondR > 0:     # 나중에 움직이는 구슬 또한 색에 따라 부호가 다르기 때문에 바꿔준다.
                    secondR += di[d]
                    secondC += dj[d]
                else:
                    secondR -= di[d]
                    secondC -= dj[d]
                if arr[abs(secondR)][abs(secondC)] == 'O':      # 구멍을 만나면
                    if secondR > 0:
                        Redhole = True
                    else:
                        Bluehole = True
                    break
                elif arr[abs(secondR)][abs(secondC)] == '#' or (abs(secondR)== abs(firstR) and abs(firstC) == abs(secondC)):        # 벽을 만나거나 먼저 움직인 구슬을 만나면
                    if secondR > 0 or secondC > 0:
                        secondR -= di[d]
                        secondC -= dj[d]
                    elif secondR < 0 or secondC < 0:
                        secondR += di[d]
                        secondC += dj[d]
                    break
            if Redhole and not Bluehole:        # 빨간 구슬만 구멍에 떨어지면
                ans = count
                flag = True
                break
            elif not Redhole and not Bluehole and (firstR1 != firstR or firstC1 != firstC or secondR1 != secondR or secondC1 != secondC):       # 두 구슬 모두 구멍에 빠지지 않고, 기울이기 전 좌표와 기울인 후의 좌표가 다르면(시간 단축을 위해)
                queue.append([firstR, firstC, secondR, secondC, count+1])
        if flag:        # 빨간 구슬만 떨어졌으면 break
            break

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
Rr = Rc = Br = Bc = 0   # 초기 빨간, 파란 구슬 위치 좌표
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            Rr, Rc = i, j
            arr[i][j] = '.'     # 좌표로만 구슬을 이동할 것이기 때문에 빈 공간으로 바꾼다.
        elif arr[i][j] == 'B':
            Br, Bc = -i, -j     # 구슬의 색깔 구분을 +, -로 하기 위해 파란 구슬 좌표는 -로 저장
            arr[i][j] = '.'
ans = 0
tilt(Rr, Rc, Br, Bc, 1)     #(빨간구슬 i, j / 파란구슬 i, j)
if ans > 0:
    print(ans)
else:
    print(-1)