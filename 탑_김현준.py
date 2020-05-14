def solution(heights):
    answer = [0]*len(heights)
    for i in range(len(heights)-1, 0, -1):  # 오른쪽 탑부터 탐색
        for j in range(i-1, -1, -1):    # i탑보다 왼쪽에 있는 탑 탐색
            if heights[i] < heights[j]:
                answer[i] = j+1  # 가능한 탑 탐색후 저장
                break
    return answer