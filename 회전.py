T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    print('#{} {}'.format(test_case, nums[M%N]))