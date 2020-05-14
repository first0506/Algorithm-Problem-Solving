T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    times = []
    for _ in range(N):
        times.append(list(map(int, input().split())))
    times = sorted(times, key=lambda x:x[1])
    end = times[0][0]
    cnt = 1
    for i in range(1, N):
        if end <= times[i][0]:
            end = times[i][1]
            cnt += 1
    print('#{} {}'.format(test_case, cnt))