def solution(dartResult):
    ans = []    # 철자별 획득 점수 리스트
    index = -1  # 철자 인덱스
    for j in range(len(dartResult)):
        i = dartResult[j]   # 앞에서부터 한글자씩
        if i=='S':
            pass
        elif i=='D':
            ans[index] = ans[index]**2  #   2제곱
        elif i=='T':
            ans[index] = ans[index]**3  #   3제곱
        elif i=='*':
            ans[index] *= 2 # 2배
            if index >0:
                ans[index-1] *= 2   # 그 전에 얻은 점수가 있으면 그 전 것도 2배
        elif i=='#':
            ans[index] *= -1    # 마이너스
        else:
            if i=='1' and  dartResult[j+1]=='0':    # 입력으로 10이 들어올 때
                ans.append(10)
                index += 1  
            elif i=='0' and index >0 and ans[index]==10:    # 10일 때 뒤의 0은 계산에서 제외해줘야하므로 건너뛰기
                pass
            else:
                ans.append(int(i))
                index += 1
    answer = sum(ans)
    return answer