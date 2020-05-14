T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    station = [0] * 5001
    bus = []
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            station[i] += 1
    print('#{}'.format(test_case), end =' ')
    P = int(input())
    for i in range(P):
        if i == P-1:
            j = int(input())
            print(station[j])
        else:
            j = int(input())
            print(station[j], end=' ')