T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    ans = 0
    containers.sort()
    trucks.sort()
    for i in range(N-1, -1, -1):
        container = containers[i]
        if container <= trucks[-1]:
            ans += container
            trucks.pop()
            if not trucks:
                break
    print('#{} {}'.format(test_case, ans))