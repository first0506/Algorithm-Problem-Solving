def back(i, visited, val, cnt): # (현재위치, visited, 경로 가중치의 합, 몇번쨰 도시인지
    global min_val
    if cnt == N and i == 0: # 모든 도시를 돌고 다시 처음 도시인 0번 도시로 왔을 때
        if val < min_val:
            min_val = val
    else:
        for j in range(N):
            if not visited[j] and arr[i][j]: # 일반적인 백트래킹 구조
                val += arr[i][j]
                visited[j] = 1
                back(j, visited[:], val, cnt+1)
                visited[j] = 0
                val -= arr[i][j]
            elif cnt == N-1 and j == 0 and arr[i][j]: # 맨처음에 순회를 돌 때 vistied[0]=1이기 떄문에 일반적인 구조로는 다시 0으로 갈 수가 없다. 따라서 또 다른 조건을 통해 순환할 수 있도록 설정
                val += arr[i][j]
                visited[j] = 1
                back(j, visited[:], val, cnt+1)
                visited[j] = 0
                val -= arr[i][j]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 2**31-1
visited = [0] * N
visited[0] = 1 # 0번부터 시작하기 때문에 미리 visited에 1을 채운다
min_val = 2**31-1
back(0, visited, 0, 0)
print(min_val)