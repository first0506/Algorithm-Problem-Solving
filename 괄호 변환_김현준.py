def solution(p):
    def f(w):
        if not w:
            return w    # 입력이 빈 문자열인 경우, 빈 문자열을 반환
        cnt1, cnt2 = 0, 0   # 앞에서부터 '(', ')' 개수
        for i in range(len(w)):
            if w[i]=='(':
                cnt1 += 1
            else:
                cnt2 += 1
            if cnt1 and cnt1==cnt2: # u가 균형잡힌 괄호일 때까지
                break
        u = w[0:i+1]
        v = w[i+1:]
        if check(u):    # u가 올바른 괄호 문자열일 때
            return u+f(v)
        else:   # 아니면
            tmp = '('+f(v)+')'
            u = u[1:-1] # 양쪽 문자 제거
            for i in u: # 괄호 방향 뒤집기
                if i=='(':
                    tmp += ')'
                else:
                    tmp += '('
            return tmp

    def check(w):   # 올바른 괄호 문자열인지 체크
        stack = []
        for i in w:
            if stack and i==')' and stack[-1]=='(': # 짝이 맞을 때
                stack.pop()
            else:
                stack.append(i) # 안 맞으면 append
        if stack:
            return False    # stack에 남으면 False
        else:  
            return True     # 없으면 올바른 괄호 문자열
        
    if check(p):    # 올바른 괄호 문자열이면 바로 출력
        answer = p
    else:
        answer = f(p)
    return answer

p = "(()())()"
# result = "(()())()"

# p = ")("
# # result = "()"

# p = "()))((()"
# # result = "()(())()"

print(solution(p))