# def solution(stones, k):
#     answer = 0
#     while 1:
#         flag = False
#         for i in range(len(stones)-k+1):
#             if not stones[i]:
#                 for j in range(k):
#                     if stones[i+j]:
#                         break
#                 else:
#                     flag = True
#                     break
#         if flag:
#             break
#         min_stone = 200000000
#         for stone in stones:
#             if 0<stone<min_stone:
#                 min_stone = stone
#         for i in range(len(stones)):
#             if stones[i]:
#                 stones[i] -= min_stone
#         answer += min_stone
#     return answer

def solution(stones, k):
    min_big = 200000000
    start = 0
    while 1:
        if start > len(stones)-k:
            break
        m = 0
        val = 0
        for i in range(start, start+k):
            if stones[i] >=val:
                m = i
                val = stones[i]
        if val < min_big:
            min_big = val
        else:
            start = m+1
    answer = min_big
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))