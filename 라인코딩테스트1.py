def solution(inputString):
    answer = 0
    stack = []
    op=['(', '{', '[', '<']
    cl=[')', '}', ']', '>']
    for i in inputString:
        if i in op:
            stack.append(i)
        elif i in cl:
            if not stack:
                answer = -1
                break
            else:
                a = stack.pop()
                if a in op:
                    answer +=1
                else:
                    answer = -1
                    break
    return answer

inputString = 'Hello, world!'
# inputString = 'line [plus]'
# inputString = 'if (Count of eggs is 4.) {Buy milk.}'
# inputString = '>_<'
print(solution(inputString))