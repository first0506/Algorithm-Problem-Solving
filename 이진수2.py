T = int(input())
for test_case in range(1, T+1):
    N = float(input())
    ans = ''
    for i in range(1, 14):
        if N>=2**(-i):
            ans += '1'
            N -= 2**(-i)
        else:
            ans += '0'
        if not N:
            break
    else:
        ans = 'overflow'
    print('#{} {}'.format(test_case, ans))