def move(t, y, num, arr):
    if t==1:
        # 다른 블록을 만날 때까지 이동
        for i in range(6):
            if arr[i][y]:
                # 해당 위치에 블록 숫자 저장
                arr[i-1][y] = num
                break
        # 블록이 아무것도 없을 때
        else:
            arr[i][y] = num
    # 나머지 블록도 동일
    elif t==2:
        for i in range(6):
            # 블록타입 2나 3는 두 개가 이어져있어 둘다 모두 고려해야 한다.
            if arr[i][y] or arr[i][y+1]:
                arr[i-1][y], arr[i-1][y+1] = num, num
                break
        else:
            arr[i][y], arr[i][y+1] = num, num
    elif t==3:
        for i in range(6):
            if arr[i][y]:
                arr[i-2][y], arr[i-1][y] = num, num
                break
        else:
            arr[i-1][y], arr[i][y] = num, num
    return arr

def down(arr):
    while 1:
        # 아래로 이동한 블록이 있는지
        flag = False
        # 아래서부터 확인
        for i in range(4, -1, -1):
            for j in range(4):
                # 블록이 있고, 바로 아래칸에 빈칸일 때
                if arr[i][j] and not arr[i+1][j]:
                    # 타입 2번의 블록 경우, 오른쪽에 블록이 현재 블록과 같고,
                    if j<3 and arr[i][j]==arr[i][j+1]:
                        # 그 블록 아래도 빈칸이면
                        if not arr[i+1][j+1]:
                            # 블록 한 칸씩 내리기
                            arr[i+1][j], arr[i+1][j+1] = arr[i][j], arr[i][j+1]
                            arr[i][j], arr[i][j+1] = 0, 0
                            flag = True
                    # 타입 2번의 블록 경우, 왼쪽에 있을 때 비교
                    elif 0<j and arr[i][j-1]==arr[i][j]:
                        if not arr[i+1][j-1]:
                            arr[i+1][j-1], arr[i+1][j] = arr[i][j-1], arr[i][j]
                            arr[i][j-1], arr[i][j] = 0, 0
                            flag = True
                    # 타입 1번이거나 3번일 때 블록 아래로 내리기 (타입3번의 경우 하나씩 분리해서 내려도 결과는 같다.)
                    else:
                        arr[i+1][j] = arr[i][j]
                        arr[i][j] = 0
                        flag = True
        # 아래로 내린 블록이 없으면 종료
        if not flag:
            return

def remove(arr):
    global ans
    while 1:
        # 타일이 가득찼는지 flag
        flag = False
        # 한 행씩 보면서 타일이 가득찼으면
        for i in range(5, 1, -1):
            if 0 not in arr[i]:
                # 블록 제거
                arr[i] = [0, 0, 0, 0]
                ans += 1
                flag = True
        # 블록을 제거 했으면 아래로
        if flag:
            down(arr)
        # 타일이 가득차지 않았으면 연한 칸에 블록이 있는지 확인
        else:

            # 1번 행렬에 블록이 있으면
            if sum(arr[1]):
                cnt = 1
                # 0번 행렬까지 블록이 있을 때
                if sum(arr[0]):
                    cnt += 1
                # cnt만큼 앞에 빈 칸을 더해주고 뒤에 칸은 없앤다
                for _ in range(cnt):
                    arr = [[0, 0, 0, 0]] + arr
                    arr.pop()
                # 블록 아래로
                down(arr)
            # 연한 칸에도 블록이 없으면 종료
            else:
                break
    return arr

N = int(input())
# 초록영역과 파란영역 따로 저장 (파란영역을 y=x축 대칭하면 초록영역과 같다.)
green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]
ans = 0

for num in range(1, N+1):
    t, x, y = map(int, input().split())
    # 블록 이동 (블록별로 번호를 매긴다)
    move(t, y, num, green)
    # 블록도 y=x축 대칭한다.
    if t==2:
        t = 3
    elif t==3:
        t = 2
    move(t, x, num, blue)
    # 블록 제거 및 밑으로
    green = remove(green)
    blue = remove(blue)
# 남은 블록 개수 세기
left = 0
for i in range(2, 6):
    for j in range(4):
        if green[i][j]:
            left += 1
        if blue[i][j]:
            left += 1

print(ans)
print(left)