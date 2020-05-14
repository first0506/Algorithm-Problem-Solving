T = int(input())
for test_case in range(1, T+1):
    E, N = map(int, input().split())
    a = list(map(int, input().split()))
    nodes = [N]
    for i in range(len(a)):
        if not i%2:
            if a[i] in nodes:
                nodes.append(a[i+1])
    print('#{} {}'.format(test_case, len(nodes)))