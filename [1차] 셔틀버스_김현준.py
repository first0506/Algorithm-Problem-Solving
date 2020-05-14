def solution(n, t, m, timetable):
    answer = ''
    times = [[] for _ in range(n)]  # 셔틀 도착 시간 리스트
    timetable.sort()    # 크루 도착시간 정렬
    line = [0]*n    # 시간별 대기열의 사람 수
    for i in range(n):
        minute = t*i
        hour = 9+minute//60
        minute %= 60
        times[i] = [hour, minute]   # 시, 분으로 이루어진 셔틀 도착 시간 리스트 추가
    for time in timetable:  # 크루별 도착시간
        hour, minute = int(time[:2]), int(time[3:])
        for i in range(n):
            if hour < times[i][0] or (hour == times[i][0] and minute <= times[i][1]):   # 셔틀 도착이 크루 도착 보다 늦을 경우
                if line[i] < m: # 대기열에 설 수 있으면
                    line[i] += 1
                else:
                    for k in range(i+1, n): # 설 수 없으면 다음 설 수 있는 셔틀 도착 시간 찾기
                        if line[k] < m:
                            line[k] += 1
                            break
                break
    for i in range(n-1, -1, -1):    # 제일 늦게 도착해야하므로 뒤에서 부터 탐색
        if line[i] < m:     # 콘이 대기열에 설 수 있을 때
            hour = str(times[i][0])
            if times[i][0] == 9:    # 시가 9시면 숫자가 한자리수 이므로 0을 앞에 붙여준다
                hour = '0'+hour
            minute = str(times[i][1])
            if times[i][1] < 10:    # 분이 한자리면 0을 앞에 붙여준다.
                minute = '0'+minute
            answer = hour+':'+minute
            break
        elif line[i] == m:  # 대기열이 꽉차면 맨 뒤에 서있는 크루 보다 앞서 도착하면 된다.
            hour, minute = int(timetable[sum(line[:i+1])-1][:2]), int(timetable[sum(line[:i+1])-1][3:]) # 맨 뒤에 서있는 크루의 도착시간
            if minute == 0: # 도착시간이 0분이면 앞선 59분에 도착
                minute = 59
                hour -= 1
            else:   # 아니면 1분 빼기
                minute -= 1
            if hour < 10:
                hour = '0'+str(hour)
            else:
                hour = str(hour)
            if minute < 10:
                minute = '0'+str(minute)
            else:
                minute = str(minute)
            answer = hour+':'+minute
            break
    return answer


print(solution(10, 60, 2, ['23:59','23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59']))