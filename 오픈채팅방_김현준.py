def solution(record):
    answer = []
    user = {}
    states = []
    for i in record:
        if len(i.split())==3:
            state, id, nickname = i.split()
            user[id] = nickname
        else:
            state, id = i.split()
        states.append([state, id])
    for i in states:
        if i[0]=='Enter':
            answer.append(user[i[1]]+'님이 들어왔습니다.')
        elif i[0]=='Leave':
            answer.append(user[i[1]]+'님이 나갔습니다.')
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

print(solution(record))