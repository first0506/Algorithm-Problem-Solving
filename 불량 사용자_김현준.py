def solution(user_id, banned_id):
    case = [[] for _ in range(len(banned_id))]  # 각 불량사용자별 가능한 제재 아이디 저장
    for k in range(len(banned_id)):
        ban = banned_id[k]
        for user in user_id:    # 불량사용자와 유저 아이디 길이 같을 때
            if len(ban)==len(user):
                for i in range(len(ban)):
                    if ban[i]!='*' and ban[i]!=user[i]: # 하나라도 다르면 break
                        break
                else:
                    case[k].append(user)    # 아니면 case에 저장
    answer = f(0, [], case, 0, banned_id, [])
    return answer

def f(n, tmp, case, answer, banned_id, result): # 순열 진행,  tmp:순열 임시 저장, result:가능한 순열 set으로 저장
    if len(tmp)==len(banned_id):    # 제재 아이디 모두 골랐을 때
        if set(tmp) not in result:  # result에 없으면 answer +1
            answer += 1
            result.append(set(tmp))
    else:
        for i in case[n]:
            if i not in tmp:
                tmp.append(i)
                answer = f(n+1, tmp, case, answer, banned_id, result)
                tmp.pop()
    return answer

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "abc1**"]     # 2
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]    # 2
# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]      #3

print(solution(user_id, banned_id))