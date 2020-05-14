def solution(n, weak, dist):        # bfs 사용 (시간초과 4개)
    from _collections import deque
    answer = 0
    dist.sort(reverse=True)     # 거리가 긴 친구부터 수리 시작하도록 정렬
    N = len(dist)

    q = deque([[weak, 0]])
    while q:
        leftover, idx = q.popleft()     # 수리가 남은 지점, 친구의 인덱스
        if not leftover:
            answer = idx
            break
        elif idx==N:
            pass
        else:
            for i in leftover:  # 수리 시작 지점
                tmp = []
                for k in leftover:  # 수리 끝나는 지점 찾기
                    if (k-i)%n > dist[idx]:     # 원행렬 인덱스 사용 - 친구의 거리보다 수리 지점간 사이가 길면 tmp저장
                        tmp.append(k)
                q.append([tmp, idx+1])
    if leftover:
        answer = -1

    return answer

def solution(n, weak, dist):    # dfs 사용 (시간초과 2개) - 위의 내용과 동일
    answer = 2**31-1
    dist.sort(reverse=True)
    N = len(dist)

    def dfs(leftover, idx):
        nonlocal answer
        if not leftover:
            answer = idx
        elif idx>=answer or idx==N:
            pass
        else:
            for i in leftover:
                tmp = []
                for k in leftover:
                    if (k-i)%n > dist[idx]:
                        tmp.append(k)
                dfs(tmp, idx+1)
    dfs(weak, 0)
    if answer==2**31-1:
        answer = -1

    return answer

def solution(n, weak, dist):        # 순열 이용 (통과)
    from itertools import permutations
    answer = -1
    N = len(dist)

    def repair(order):
        for w in weaks:
            cur_friend = 0  # 수리하는 친구의 인덱스
            cur_repair = 0  # 친구가 수리를 시작한 지점 인덱스
            i = 1
            while cur_repair+i < len(w) and cur_friend < len(order):    # 수리를 모두 마치거나, 수리 불가능할 때까지
                if w[cur_repair+i]-w[cur_repair] > order[cur_friend]:
                    cur_repair += i
                    cur_friend += 1
                    i = 1
                else:
                    i += 1
            if cur_repair+i > len(w) or cur_friend < len(order):    # 수리를 모두 마쳤거나, 친구가 덜 필요하면
                return True
        return False

    weaks = []      # 수리 시작하는 지점에 따라 원행렬을 직선으로 펼쳐 모두 저장
    for _ in range(len(weak)):
        weaks.append(weak[:])
        a = weak.pop(0)
        weak.append(a+n)    # [1, 5, 6, 10], [5, 6, 10, 13], [6, 10, 13, 17], [10, 13, 17, 18]

    for i in range(1, N+1):     # 필요한 친구수 별로 친구들의 순서 순열 찾기
        orders = permutations(dist, i)  # i = 필요한 친구수, orders = i명 필요할 때 친구들의 순서 순열 저장
        flag = False
        for order in orders:
            if repair(order):   # 수리가 완료되면
                answer = i
                flag = True
                break
        if flag:
            break

    return answer

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
# result = 2

# n = 12
# weak = [1, 3, 4, 9, 10]
# dist = [3, 5, 7]
# # result = 1

# n = 50
# weak = [1, 5, 10, 16, 22, 25]
# dist = [3, 4, 6]
# # result = 3

print(solution(n, weak, dist))