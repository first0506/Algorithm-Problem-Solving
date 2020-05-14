def solution(user_id, banned_id):
    answer = 0
    used = [0]*len(user_id)
    cnt = [0]*len(banned_id)
    for unum in range(len(user_id)):
        if not used[unum]:
            


    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
print(solution(user_id, banned_id))