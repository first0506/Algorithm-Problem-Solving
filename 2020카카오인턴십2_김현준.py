def solution(expression):
    answer = 0
    buho = ['+', '-', '*']
    exp = []
    tmp = ''
    for i in expression:
        if i in buho:
            exp.append(int(tmp))
            exp.append(i)
            tmp = ''
        else:
            tmp += i
    exp.append(int(tmp))
    buhos = []
    def f(n, tmp):
        nonlocal buhos, buho
        if n==3:
            buhos.append(tmp[:])
        else:
            for i in buho:
                if i not in tmp:
                    tmp.append(i)
                    f(n+1, tmp[:])
                    tmp.pop()
    f(0, [])
    for b in buhos:
        exp1 = exp[:]
        for k in b:
            i = 0
            while k in exp1:
                if exp1[i]==k:
                    if k=='*':
                        a = exp1.pop(i+1)
                        exp1.pop(i)
                        c = exp1.pop(i-1)
                        exp1.insert(i-1, c*a)
                    elif k=='+':
                        a = exp1.pop(i+1)
                        exp1.pop(i)
                        c = exp1.pop(i-1)
                        exp1.insert(i-1, c+a)
                    elif k=='-':
                        a = exp1.pop(i+1)
                        exp1.pop(i)
                        c = exp1.pop(i-1)
                        exp1.insert(i-1, c-a)
                    i = 0
                i += 1
        print(b)
        print(exp1[0])
        if abs(exp1[0]) > answer:
            answer = abs(exp1[0])
    return answer

# expression = "100-200*300-500+20"
# # result = 60420

# expression = "50*6-3*2"
# # result = 300

expression = '10+10*10-10'

print(solution(expression))