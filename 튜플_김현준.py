def solution(s):
    s = s[1:-1] # 양 끝 { } 제거
    s_split = []
    tmp1 = ''   # 숫자만 임시 저장
    tmp2 = []   # 같은 튜플 내 숫자들 임시 저장
    for i in range(len(s)):
        if s[i]=='{':
            pass
        elif s[i]=='}': # 튜플이 닫히면
            tmp2.append(int(tmp1))  # 임시 저장된 숫자, tmp2에 넣기
            tmp1 = ''   # tmp1 초기화
            s_split.append(tmp2[:])     
            tmp2 = []
        elif s[i]==',':
            if tmp1:    # 튜플 안의 , 일 때만 숫자 임시 저장
                tmp2.append(int(tmp1))
                tmp1 = ''
        else:
            tmp1 += s[i]    # 숫자 붙이기
    s_split = sorted(s_split, key=lambda x: len(x)) # 튜플들 길이별로 정렬
    answer = s_split[0]
    for i in range(1, len(s_split)):   
        second = s_split[i]
        first = s_split[i-1]
        answer.append(list(set(second)-set(first))[0])  # 뒤 튜플에서 앞 튜플 빼기
    return answer

# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}" # [2, 1, 3, 4]
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}" # [2, 1, 3, 4]
# s = "{{20,111},{111}}" # [111, 20]
# s = "{{123}}" # [123]
# s = "{{4,2,3},{3},{2,3,4,1},{2,3}}" # [3, 2, 4, 1]

print(solution(s))
