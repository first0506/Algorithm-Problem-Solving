T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr1 = [[0]*N for _ in range(N)]
    group = []
    big = []
    a, b = 0, 0
    for i in range(N):
        for j in range(N):
            if not arr1[i][j] and arr[i][j]:
                a = N-i
                for k in range(1, N-i):
                    if not arr[i+k][j]:
                        a = k
                        break
                b = N-j
                for k in range(1, N-j):
                    if not arr[i][j+k]:
                        b = k
                        break
                group.append([a, b, a*b])
                for m in range(i, i+a):
                    for n in range(j, j+b):
                        arr1[m][n] = 1

    for i in range(len(group)-1, 0, -1):
        for j in range(i):
            if group[j][2] > group[j+1][2]:
                group[j], group[j+1] = group[j+1], group[j]
            elif group[j][2] == group[j+1][2]:
                if group[j][0] > group[j+1][0]:
                    group[j], group[j + 1] = group[j + 1], group[j]
    print('#{} {}'.format(test_case, len(group)), end=' ')
    for i in range(len(group)):
        if i == len(group)-1:
            print('{} {}'.format(group[i][0], group[i][1]))
        else:
            print('{} {}'.format(group[i][0], group[i][1]), end= ' ')