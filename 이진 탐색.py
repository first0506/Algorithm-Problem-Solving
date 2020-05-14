T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    ans = 0
    for b in B:
        start = 0
        end = N-1
        flag = 'mid'
        while start <= end:
            mid = (start+end)//2
            if A[mid]==b:
                ans += 1
                break
            elif A[mid]>b and flag!='left':
                    end = mid-1
                    flag = 'left'
            elif A[mid]<b and flag!='right':
                    start = mid+1
                    flag = 'right'
            else:
                break
    print('#{} {}'.format(test_case, ans))