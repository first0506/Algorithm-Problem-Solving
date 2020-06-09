def solution(nums):
    answer = 0
    N = len(nums)
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                tmp = nums[i]+nums[j]+nums[k]
                for m in range(2, tmp-1):
                    if not tmp%m:
                        break
                else:
                    answer += 1
    return answer

# nums = [1,2,3,4]
# # result = 1

nums = [1,2,7,6,4]
# result = 4

print(solution(nums))