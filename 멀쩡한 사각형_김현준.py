# def solution(w, h):
#     answer = w*h
#     if max(w, h)%min(w, h):
#         oneLineBlock = max(w, h)//min(w, h) + 1
#     else:
#         oneLineBlock = max(w, h)//min(w, h)
#     sliced = oneLineBlock*min(w, h)
#     answer -= sliced
#     return answer

import math
def solution(w, h):
    answer = w*h
    a = max(w, h)/min(w, h)
    for i in range(1, min(w, h)+1):
        Min = int(a*(i-1))
        Max = math.ceil(a*i)
        answer -= Max-Min
    return answer

w = 100000000
h = 99999999
# result = 80

print(solution(w, h))