def vote(i, j, d1, d2):
    global min_val
    maps = [[0]*(N+1) for _ in range(N+1)]
    val1, val2, val3, val4, val5 = 0, 0, 0, 0, 0
    for m in range(d1+1):
        maps[i+m][j-m] = 5
    for m in range(d2+1):
        maps[i+m][j+m] = 5
    for m in range(d2+1):
        maps[i+d1+m][j-d1+m] = 5
    for m in range(d1+1):
        maps[i+d2+m][j+d2-m] = 5

    for m in range(1, i+d1):
        for n in range(1, j+1):
            if maps[m][n] == 0:
                val1 += arr[m][n]
            else:
                break
    for m in range(1, i+d2+1):
        for n in range(N, j, -1):
            if maps[m][n] == 0:
                val2 += arr[m][n]
            else:
                break
    for m in range(i+d1, N+1):
        for n in range(1, j-d1+d2):
            if maps[m][n] == 0:
                val3 += arr[m][n]
            else:
                break
    for m in range(i+d2+1, N+1):
        for n in range(N, j-d1+d2-1, -1):
            if maps[m][n] == 0:
                val4 += arr[m][n]
            else:
                break
    val5 = total-sum([val1, val2, val3, val4])
    if max(val1, val2, val3, val4, val5) - min(val1, val2, val3, val4, val5) < min_val:
        min_val = max(val1, val2, val3, val4, val5) - min(val1, val2, val3, val4, val5)

N = int(input())
arr = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
min_val = 2**31-1
total = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        total += arr[i][j]
for i in range(1, N+1):
    for j in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if i+d1+d2 <=N and 1<= j-d1 < j < j+d2 <=N:
                    vote(i, j, d1, d2)
print(min_val)