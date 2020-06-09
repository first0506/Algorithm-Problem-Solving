def solution(sticker):
    N = len(sticker)
    first = [0]*N
    first[0] = sticker[0]
    last = [0]*N
    if N>1:
        last[1] = sticker[1]
    for i in range(1, N-1):
        first[i] = sticker[i]+max(first[i-2], first[i-3])
    for i in range(2, N):
        last[i] = sticker[i]+max(last[i-2], last[i-3])
    return max(first+last)

# sticker = [14, 6, 5, 11, 3, 9, 2, 10]
# # answer = 36

# sticker = [1, 3, 2, 5, 4]
# # answer = 8

sticker = [1]

print(solution(sticker))