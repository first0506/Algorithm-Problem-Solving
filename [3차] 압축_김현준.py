def solution(msg):
    answer = []
    d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    i = 0
    while i < len(msg): # i = msg 앞에서부터 몇번째 인덱스인지
        mlen=0  # 일치하는 사전 속 단어의 길이
        mk=0    # 일치하는 사전 속 단어의 색인번호
        for k in range(len(d)):
            if ''.join(msg[i:i+len(d[k])])==d[k] and len(d[k]) > mlen:  # 사전과 일치하고, 일치하는게 두 개 이상이면 더 긴 거면
                mlen = len(d[k])
                mk = k
        d.append(''.join(msg[i:i+len(d[mk])+1]))    # 사전에 다음 글자 남아있는거 더해서 다시 등록
        i += mlen   # 일치했던 단어만큼 건너뛰고 다음 인덱스부터 시작
        answer.append(mk+1) # 색인번호 더하기(+1)
    return answer

msg = 'KAKAO'   #[11, 1, 27, 15]
# msg = 'TOBEORNOTTOBEORTOBEORNOT'    # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# msg = 'ABABABABABABABAB'    # [1, 2, 27, 29, 28, 31, 30]

print(solution(msg))