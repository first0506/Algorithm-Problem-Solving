wheels = [list(map(int, input())) for _ in range(4)]
K = int(input())
ans = 0
p = [0]*4
for _ in range(K):
    num, dir = map(int, input().split())
    same = [0]*3
    for i in range(3):
        if wheels[i][(p[i]+2)%8] != wheels[i+1][(p[i+1]-2)%8]:
            same[i] = 1
    p[num-1] = (p[num-1]-dir)%8
    used = [0]*4
    used[num-1] = 1
    queue = [[num, dir]]
    while queue:
        n, d = queue.pop(0)
        if n-1 >= 1 and not used[n-2] and same[n-2]:
            queue.append([n-1, -d])
            p[n-2] = (p[n-2]+d)%8
            used[n-2] = 1
        if n+1 <=4 and not used[n] and same[n-1]:
            queue.append([n+1, -d])
            p[n] = (p[n]+d)%8
            used[n] = 1
for i in range(4):
    ans += wheels[i][p[i]]*(2**i)
print(ans)