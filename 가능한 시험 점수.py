T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    v = [1]+[0]*sum(nums)
    for i in range(N):
        for j in range(sum(nums[:i]), -1, -1):
            if v[j]:
                v[j+nums[i]] = 1
    print('#{} {}'.format(test_case, sum(v)))