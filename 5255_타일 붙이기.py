T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    v = [0]*(N+1)
    v[0] = 1
    v[1] = 1
    v[2] = 3
    for i in range(3, N+1):
        v[i] = v[i-1] + 2*v[i-2] + v[i-3]
    print('#{} {}'.format(test_case, v[N]))