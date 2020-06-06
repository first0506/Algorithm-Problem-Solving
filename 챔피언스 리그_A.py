N = int(input())
info = []
for _ in range(N*(N-1)):
    a, m, b, n = input().split()
    m, n = int(m), int(n)
    idxa, idxb = -1, -1
    for i in range(len(info)):
        if info[i][0]==a:
            idxa=i
        elif info[i][0]==b:
            idxb=i
        if idxa!=-1 and idxb!=-1:
            break
    if idxa==-1:
        info.append([a, 0, 0])
        idxa = len(info)-1
    if idxb==-1:
        info.append([b, 0, 0])
        idxb = len(info)-1
    if m>n:
        info[idxa][1] += 1
    else:
        info[idxb][1] += 1
    info[idxa][2] += m-n
    info[idxb][2] += n-m
info.sort(key=lambda x: (-x[1], -x[2], x[0]))
for team, win, setN in info:
    print('{} {} {}'.format(team, win, setN))

input =
3
a 2 b 0
a 2 c 1
b 2 a 1
b 0 c 2
c 0 a 2
c 1 b 2
result =
a 3 4
b 2 -2
c 1 -2

input =
4
drx 2 t1 1
drx 1 gen 2
t1 1 gen 2
t1 2 drx 1
kt 1 drx 2
t1 0 kt 2
drx 2 kt 1
gen 1 t1 2
gen 2 kt 0
gen 1 drx 2
kt 0 t1 2
kt 2 gen 0
result =
drx 4 2
gen 3 0
t1 3 0
kt 2 -2