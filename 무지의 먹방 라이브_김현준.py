def solution(food_times, k):
    answer = -1
    food_sort = [(i[0]+1, i[1]) for i in sorted(enumerate(food_times), key = lambda x : x[1])]  # 음식 먹는데 필요한 시간순으로 정렬(이 때 음식의 번호또한 저장)
    leftdish = len(food_times)  # 회전판에 남아있는 음식 수
    endtime = 0 # 모두 먹는데 필요한 시간
    for i in range(len(food_sort)):
        if not i:   # 음식 먹는데 필요한 시간이 가장 짧은 음식일 때
            tmp = endtime + food_sort[i][1] * leftdish  #tmp = i 번째 음식을 다 먹는 턴이 끝나는 시간
        else:
            tmp = endtime + (food_sort[i][1]-food_sort[i-1][1]) * leftdish
        if k < tmp: # 턴이 끝나는 시간이 k보다 크면
            pan = food_sort[i::]    # pan = 회전판에 있는 음식들
            pan = sorted(pan, key=lambda x : x[0])  # 번호순으로 다시 정렬
            answer = pan[(k-endtime)%leftdish][0]   # i-1 번째 음식을 다 먹는 턴 이후 k초에 먹는 음식 찾기
            break
        leftdish -= 1
        endtime = tmp
    return answer

food_times = [3, 1, 2]
k = 5   # 1

print(solution(food_times, k))