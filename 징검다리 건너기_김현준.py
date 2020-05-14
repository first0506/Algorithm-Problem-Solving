# def solution(stones, k):
#     answer = 2**31-1
#     i = 0
#     while i < len(stones)-k+1:
#         maxval = 0
#         index = 0
#         for j in range(i+k-1, i-1, -1):
#             if stones[j] > maxval:
#                 maxval = stones[j]
#                 index = j
#         if maxval <= answer:
#             answer = maxval
#         i = index+1
#     return answer

def solution(stones, k):    # k 징검다리씩 검사(k개 돌 중 가장 큰 돌 찾기)
    answer = 2**31-1
    i = 0
    while i < len(stones)-k+1:
        for j in range(i+k-1, i-1, -1):
            if stones[j] > answer:  # answer보다 큰 돌이 있으면 어차피 불가능하므로 건너뛰기
                i = j+1 # answer보다 큰 돌 +1로 이동
                break
        else:
            answer = max(stones[i:i+k]) # answer보다 큰 돌이 없으면 k개 돌 중 가장 큰 돌 저장, 건너뛰기
            i = stones[i:i+k].index(answer)+i+1
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3   # 3

print(solution(stones, k))