def solution(s):
    answer = []
    t = []
    num = ''
    ts = [[] for _ in range(501)]
    for k in range(1, len(s)-1):
        i = s[k]
        if i=='{' or (i==',' and s[k+1]=='{'):
            t = []
        elif i=='}':
            t.append(num)
            ts[len(t)] = t
            num = ''
        elif i==',':
            t.append(num)
            num = ''
        else:
            num += i
    for i in range(1, 501):
        if ts[i]:
            answer.append(int(list(set(ts[i])-set(ts[i-1]))[0]))
        else:
            break
    return answer

s = "{{20,111},{111}}"
print(solution(s))