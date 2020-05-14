def perm(i, v):     # 각 사람별 어느 계단을 이용할 지
    if i == num_ppl:
        down(v)
    else:
        for m in range(2):
            v[i] = m
            perm(i+1, v)

def down(v):
    global ans
    stair1, stair2 = [], []
    for i in range(num_ppl):
        if v[i]:        #2번 계단
            stair2.append(abs(ppls[i][0]-stairs[1][0])+abs(ppls[i][1]-stairs[1][1])+1)  # 계단과 사람의 거리 구한 후 대기시간 1을 더해준다.
        else:           #1번 계단
            stair1.append(abs(ppls[i][0]-stairs[0][0])+abs(ppls[i][1]-stairs[0][1])+1)
    a, b = 0, 0
    if len(stair1) > 0:
        a = wait(stair1, stairs[0][2])  # 계단을 이용하는 사람이 있을 때
    if len(stair2) > 0:
        b = wait(stair2, stairs[1][2])

    if not a and b+stairs[1][2] < ans:  # 2번계단만 이용할 때               (마지막 사람이 계단 이용하는 시간 더해주어야한다.)
        ans = b+stairs[1][2]
    elif not b and a+stairs[0][2] < ans:    # 1번계단만 이용할 때
        ans = a+stairs[0][2]
    else:
        if max(a+stairs[0][2], b+stairs[1][2]) < ans:   # 두 계단 중 늦게 끝나는 사람 시간
            ans = max(a+stairs[0][2], b+stairs[1][2])

def wait(stair, k):
    stair.sort()    # 계단에 도착하는 시간별로 정렬
    for i in range(len(stair)):
        if i >= 3 and stair[i] < stair[i-3]+k:  # 3번쨰 앞 사람의 계단 완료 시간보다 같거나 커야한다.
            stair[i] = stair[i-3]+k
    return stair[-1]    # 마지막 사람의 계단 이용시간 추출

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ppls = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                ppls.append([i, j])
            elif arr[i][j] > 1:
                stairs.append([i, j, arr[i][j]])
    num_ppl= len(ppls)
    v = [0]*num_ppl
    ans = 100000000
    perm(0, v)
    print('#{} {}'.format(test_case, ans))