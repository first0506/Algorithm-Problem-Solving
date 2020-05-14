def solution(m, musicinfos):
    answer = ''
    m = change(m)   # 멜로디에 '#'이 붙어있는 음은 소문자로 치환
    music = []
    for i in musicinfos:
        s, e, t, n = i.split(',')   # start, end, title, note
        n = change(n)   # 악보 문자 치환
        cnt = len(n)    # 음악의 전체 음 개수
        minute = (int(e[0:2])-int(s[0:2]))*60 + (int(e[3::])-int(s[3::]))   # 전체 음악 길이(분)
        music.append([n*(minute//cnt)+n[0:(minute%cnt)], t, minute])    # [재생음악 모두 합친거(음), 제목, 전체 음악 길이]
    length = 0  # 일치하는 음악의 길이
    for i in music:
        if m in i[0] and i[2] > length: # 멜로디가 재생음악에 존재하고, 일치하는 것이 두개 이상이면 더 긴 음악 저장
            answer = i[1]
            length = i[2]
    if not answer:
        answer = '(None)'   # 일치하는 음악없으면 None
    return answer

def change(notes):
    result = ''
    for i in notes: # 앞에서부터 한 음씩 더하다가
        if i!='#':
            result += i
        else:   # '#'이 나오면
            a = result[-1]  # 그 전 음을 빼고 소문자 음을 더해준다
            if a=='C':
                result = result[:-1]+'c'
            elif a=='D':
                result = result[:-1]+'d'
            elif a=='F':
                result = result[:-1]+'f'
            elif a=='G':
                result = result[:-1]+'g'
            elif a=='A':
                result = result[:-1]+'a'
    return result

# m = 'ABCDEFG'
# musicinfos = ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']  # 'HELLO'
# m = 'CC#BCC#BCC#BCC#B'
# musicinfos = ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']  # 'FOO'
m = 'ABC'
musicinfos = ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']  # 'WORLD'

print(solution(m, musicinfos))