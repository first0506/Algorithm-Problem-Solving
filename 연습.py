# def solution(n, computers):
#     answer = 0
#     v = [0]*n
#     for i in range(n):
#         if not v[i]:
#             q = [i]
#             v[i] = 1
#             answer += 1
#             while q:
#                 k = q.pop(0)
#                 for j in range(n):
#                     if k!=j and computers[k][j] and not v[j]:
#                         v[j] = 1
#                         q.append(j)
#     return answer
#
# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# # return = 2
#
# # n = 3
# # computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# # # return = 2
#
# print(solution(n, computers))

def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money)-1): # 첫 집을 무조건 터는 경우
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)): # 마지막 집을 무조건 터는 경우
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    return max(max(dp1), max(dp2)) # 두 경우 중 최대

money = [1, 2, 3, 1]
# return = 4

print(solution(money))

