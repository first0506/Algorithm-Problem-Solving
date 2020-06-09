from heapq import heappush, heappop
def solution(N, road, K):
    answer = 0
    arr = {i+1:[] for i in range(N)}
    for a, b, c in road:
        arr[a].append([b, c])
        arr[b].append([a, c])
    times = [2**31-1]*(N+1)
    q = []
    heappush(q, [0, 1])
    while q:
        t, s = heappop(q)
        if times[s] > t:
            times[s] = t
            for end, time in arr[s]:
                time += t
                heappush(q, [time, end])
    for i in times:
        if i <= K:
            answer += 1
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
# result = 4

# N = 6
# road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
# K = 4
# # result = 4

print(solution(N, road, K))