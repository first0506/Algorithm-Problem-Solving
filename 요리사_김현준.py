def combi(i, choice, cnt): # 0번 재료를 고정으로 하고 1~ N-1번 재료 중 (N//2)-1개의 재료를 뽑는 조합 실행
    if cnt == N//2:
        S(choice)
    else:
        for j in range(i, N//2 + cnt + 1): # 백트래킹을 이용한 조합
            if choice[j] == 0:
                choice[j] = 1
                combi(j+1, choice, cnt + 1)
                choice[j] = 0

def S(choice):
    global ans
    result = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                if choice[i] == 1 and choice[j] == 1: # 뽑힌 재료들의 시너지 합
                    result += arr[i][j]
                elif choice[i] == 0 and choice[j] == 0: # 뽑히지 않은 재료들의 시너지 합
                    result -= arr[i][j]
    if abs(result) < ans:
        ans = abs(result)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    choice = [1] + [0] * (N-1) # 두 가지 팀으로 나누는 경우의 수는 하나의 원소를 고정으로 뽑고 나머지는 조합을 통해 구한다.(이 경우엔 0번 재료를 고정)
    ans = 2**31-1
    combi(1, choice, 1)
    print('#{} {}'.format(test_case, ans))