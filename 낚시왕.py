def catch(ppl):
    global ans
    r = R
    a = 0
    flag = False
    for shark_idx in range(len(sharks)):
        if sharks[shark_idx][1] == ppl and sharks[shark_idx][4]:
            if sharks[shark_idx][0] < r:
                r = sharks[shark_idx][0]
                a = shark_idx
                flag = True
    if flag:
        ans += sharks[a][4]
        sharks[a][4] = 0

def move():
    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, 1, -1]
    for shark_idx in range(len(sharks)):
        if sharks[shark_idx][4]:
            if sharks[shark_idx][3] in [1, 2]:
                a = (sharks[shark_idx][2]) % ((R - 1) * 2)
                if sharks[shark_idx][3] == 1:
                    if a-(sharks[shark_idx][0]+1) < 0:
                        sharks[shark_idx][0] -= a
                    elif 0<= a-(sharks[shark_idx][0]+1) < R:
                for _ in range((sharks[shark_idx][2]) % ((R - 1) * 2)):
                    ni = sharks[shark_idx][0] + di[sharks[shark_idx][3]]
                    if 0 <= ni < R:
                        sharks[shark_idx][0] = ni
                    else:
                        sharks[shark_idx][3] = 3 - sharks[shark_idx][3]
                        sharks[shark_idx][0] += di[sharks[shark_idx][3]]
            else:
                for _ in range((sharks[shark_idx][2]) % ((C - 1) * 2)):
                    nj = sharks[shark_idx][1] + dj[sharks[shark_idx][3]]
                    if 0 <= nj < C:
                        sharks[shark_idx][1] = nj
                    else:
                        sharks[shark_idx][3] = 7 - sharks[shark_idx][3]
                        sharks[shark_idx][1] += dj[sharks[shark_idx][3]]

    for shark_idx1 in range(len(sharks)-1):
        if sharks[shark_idx1][4]:
            for shark_idx2 in range(shark_idx1+1, M):
                if sharks[shark_idx2][4]:
                    if [sharks[shark_idx1][0], sharks[shark_idx1][1]] == [sharks[shark_idx2][0], sharks[shark_idx2][1]]:
                        if sharks[shark_idx1][4] > sharks[shark_idx2][4]:
                            sharks[shark_idx2][4] = 0
                        else:
                            sharks[shark_idx1][4] = 0
                            break

R, C, M = map(int, input().split())
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append([r-1, c-1, s, d, z])
ans = 0
for ppl in range(C):
    catch(ppl)
    move()
print(ans)