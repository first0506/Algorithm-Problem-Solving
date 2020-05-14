def perm(cnt, buhos, result):
    a = ['+', '-', '*', '/']
    if cnt == N-1:
        sik = [0] * (2 * N - 1)
        for i in range(N - 1):
            sik[2 * i] = numbers[i]
            sik[2 * i + 1] = result[i]
        sik[-1] = numbers[-1]
        cal(sik)
    for i in range(4):
        if buhos[i]:
            buhos[i] -= 1
            result[cnt] = a[i]
            perm(cnt+1, buhos, result)
            buhos[i] += 1

def cal(sik):
    global max_val, min_val
    point = 1
    result = sik[0]
    while point < len(sik):
        if sik[point] == '+':
            result += sik[point+1]
            point += 2
        elif sik[point] == '-':
            result -= sik[point+1]
            point += 2
        elif sik[point] == '*':
            result *= sik[point+1]
            point += 2
        elif sik[point] == '/':
            if result<0:
                result = -((-result)//sik[point+1])
                point += 2
            else:
                result = result // sik[point+1]
                point += 2
    if result > max_val:
        max_val = result
    if result < min_val:
        min_val = result

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    buhos = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_val = -(2**31-1)
    min_val = 2**31-1
    buhos1 = []
    perm(0, buhos, ['']*(N-1))
    print('#{} {}'.format(test_case, max_val-min_val))

# 선생님 강의 자료
# def f(n, k, r, op1, op2, op3, op4):
#     global
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     op1, op2, op3, op4 = map(int, input().split())
#     card = list(map(int, input().split()))
#     minV = 10000000000
#     maxV = -10000000000
#     f(1, N, card[0], op1, op2, op3, op4)
#     print('#{} {}')

# 순열
def c(n, w):
    global M, max_ans, min_ans
    if n == M:
        print(w)
        ans = calc(w, num[:])
        # if ans:         이거 있어서 오류남
        if ans > max_ans:
            max_ans = ans
        if ans < min_ans:
            min_ans = ans
    else:
        for i in range(M):
            # 중복된 원소를 가진 순열 처리
            if not v[i] and (i == 0 or operator[i-1] != operator[i] or v[i-1]):
                v[i] = 1
                w[n] = operator[i]
                c(n+1, w)
                v[i] = 0
# 계산
def calc(w, num): # i: O 인덱스
    ans = num.pop(0)
    for j in range(M):
        if not w[j]:
            ans += num.pop(0)
        if w[j] == 1:
            ans -= num.pop(0)
        if w[j] == 2:
            ans *= num.pop(0)
        if w[j] == 3:
            x = num.pop(0)
            if x != 0:          # 분모가 0이 아닐 때
                if ans < 0:     # 분자가 0보다 작을 때
                    ans = -((-ans)//x)
                elif ans >= 0:  # 분자가 0보다 클 때
                    ans //= x
    return ans

T = int(input())
for t in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split())) # +, -, *, / 순서
    num = list(map(int, input().split()))
    max_ans = -2**31+1
    min_ans = 2**31-1

    # 연산자 숫자로 설정 ex) 2 1 0 1 => 0 0 1 3
    operator = []  # 0: '+' / 1: '-' / 2: '*' / 3: '/'
    for x in range(len(temp)):
        for y in range(temp[x]):
            operator.append(x)

    # 연산자 순열(중복X)
    M = len(operator)
    v = [0] * M  # 방문 여부 리스트
    w = [0] * M  # 임시, 순열 담는 리스트
    c(0, w)
    final = max_ans - min_ans
    if final == -4294967294:  # 혹시 몰라서 넣은 예외처리ㅠ
        final = 0

    print('#{0} {1}'.format(t, final))