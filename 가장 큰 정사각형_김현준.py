n, m = map(int, input().split())
arr = [[0]*(m+2)] + [[0]+list(map(int, list(input())))+[0] for _ in range(n)] + [[0]*(m+2)] # 0으로 감싸기
ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i][j]:   # 0이 아닐 때
            arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])+1  # 왼쪽위, 위, 왼쪽 숫자 중 가장 작은 값 + 1 (가능한 가장 큰 정사각형 변의 길이)
            if arr[i][j] > ans:
                ans = arr[i][j]
print(ans**2)   # 넓이 = 제곱