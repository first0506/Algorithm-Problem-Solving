def solution(road, n):
    answer = -1
    queue = [[0, 0, 0]]
    while 1:
        cur, bosu, max_l = queue.pop(0)
        if cur==len(road):
            if max_l > answer:
                answer = max_l
            break
        if road[cur]=='1':
            queue.append([cur+1, bosu, max_l+1])
        else:
            if bosu < n:
                queue.append([cur+1, bosu+1, max_l+1])
            if max_l > answer:
                answer = max_l
            queue.append([cur+1, bosu, 0])
    return answer

road ="111011110011111011111100011111"
n =	3
# road ="001100"
# n =	5
print(solution(road, n))