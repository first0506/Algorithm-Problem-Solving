def colorpaper():
    global ans
    if sum(size) > ans: # 최소 색종이 결과값보다 현재 색종이 개수가 많으면 break
        return
    for s in size:  # 한 종류의 색종이도 5개 초과면 break
        if s > 5:
            return

    a, b = 0, 0
    for m in range(10):
        for n in range(10):
            if arr[m][n] == 1:  # 덮을 1의 위치 탐색
                a, b = m, n
                break
        if arr[m][n]:
            break
    else:
        if sum(size) < ans:     # 덮을 1이 없으면 색종이 결과값 비교
            ans = sum(size)

    for s in range(5, 0, -1):   # 색종이 크기가 5인 것부터 차례로 덮어보기
        if possible(a, b, s):   # 덮을 수 있다면
            size[s-1] += 1      # 해당 색종이 개수 +1
            for r in range(a, a+s):
                for c in range(b, b+s):
                    arr[r][c] = 0   # 덮은 영역 0으로
            colorpaper()    # 재귀반복
            size[s-1] -= 1      # 재귀 반복 전 행동 원위치
            for r in range(a, a+s):
                for c in range(b, b+s):
                    arr[r][c] = 1

def possible(i, j, s):
    if i+s-1 <10 and j+s-1 <10:     # 색종이가 판을 넘는지 안넘는지
        for m in range(i, i+s):
            for n in range(j, j+s):
                if arr[m][n] == 0:  # 하나라도 0이면 False
                    return False
        return True # 모두 돌았으면 True
    else:
        return False

arr = [list(map(int, input().split())) for _ in range(10)]
size = [0]*5
ans = 2**31-1
colorpaper()

if ans == 2**31-1:  # 덮을게 하나도 없으면
    ans = -1
print(ans)