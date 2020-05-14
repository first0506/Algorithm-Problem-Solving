def solution(n):
    n -= 1  # 3진법과 같게 만들기 위해서
    change = [1, 2, 4]
    answer = ''
    while 1:
        print(answer)
        answer = str(change[n%3]) + answer  # 나머지를 뒤쪽에 붙임
        if n//3==0:
            break
        else:
            answer = solution(n//3)+answer  # 몫이 1이상이면 재귀 반복
            break
    return answer

solution(150)   # 결과 중간값을 확인하면 이해하기 쉬울 것