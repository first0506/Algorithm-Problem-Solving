def solution(n, t, m, p):
    total = ''  # 모든 N진수 게임 숫자 모음
    num = 0 # N진수 변환 전 10진수 숫자
    while len(total) < (t-1)*m+p:   # 튜브가 말해야 하는 숫자 t개까지 num 증가
        total += change(num, n, '')
        num += 1
    answer = total[p-1:(t-1)*m+p+1:m]   # total에서 튜브 순서의 숫자만 고르기
    return answer

def change(num, n, result): # N진수 변환
    b = num % n
    if b == 10:
        result = 'A' + result
    elif b == 11:
        result = 'B' + result
    elif b == 12:
        result = 'C' + result
    elif b == 13:
        result = 'D' + result
    elif b == 14:
        result = 'E' + result
    elif b == 15:
        result = 'F' + result
    else:
        result = str(b) + result
    a = num//n
    if a:
        return change(a, n, result) # 재귀(n으로 계속 나눠줌)
    else:
        return result

# n, t, m, p = 2, 4, 2, 1
n, t, m, p = 16, 16, 2, 1
# n, t, m, p = 16, 16, 2, 2
print(solution(n, t, m, p))