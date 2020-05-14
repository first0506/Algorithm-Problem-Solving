def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower() # 대소문자 구분 없기 때문에 모두 소문자로
    A1, A2 = [], [] # 두 글자 다중집합
    for i in range(len(str1)-1):
        for k in str1[i:i+2]:   # 두 글자 중 하나라도
            if not k.isalpha(): # 문자열이 아니면(공백, 숫자, 특수문자)
                break
        else:
            A1.append(str1[i:i+2])  # 두 글자 모두 문자열이면 리스트에 추가
    for i in range(len(str2)-1):
        for k in str2[i:i+2]:
            if not k.isalpha():
                break
        else:
            A2.append(str2[i:i+2])
    if not A1 and not A2:   # 모두 공집합이면 J(A,B)=1  -> 1*65536
        answer = 65536
    else:
        v = [0]*len(A2) # A2 원소 중복 check
        gop = 0 # 교집합 원소 개수
        for i in A1:
            for k in range(len(A2)):
                if i==A2[k] and not v[k]:   # A1, A2 원소가 같고, A2 원소 비교 안했었으면
                    gop += 1
                    v[k] = 1
                    break
        hap = len(A1) + len(A2) - gop   # 합집합 원소 개수
        answer = int(65536*(gop/hap))
    return answer

print(solution('aa1+aa2', 'AAAA12'))