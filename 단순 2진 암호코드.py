T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    codes = [input() for _ in range(N)]
    ans = 0
    result = []
    for i in range(N):
        if '1' in codes[i]:
            code = codes[i]
            break
    compare = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    for i in range(M-1, -1, -1):
        if code[i]=='1':
            code = code[i-55:i+1]
            break
    for i in range(0, 56, 7):
        a = code[i:i+7]
        for j in range(10):
            if a==compare[j]:
                result.append(j)
                break
    if not (sum([result[i] for i in range(0, 8, 2)])*3 + sum([result[i] for i in range(1, 7, 2)]) + result[-1])%10:
        ans = sum(result)
    print('#{} {}'.format(test_case, ans))