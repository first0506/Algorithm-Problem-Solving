from heapq import heappush, heappop

N, M = map(int, input().split())
class Node():
    def __init__(self, name, cost):
        self.next = [(name, cost)]

    def addDiscipline(self, name, cost):
        self.next.append((name, cost))
info = {}
for _ in range(M):
    pre, post, cost = input().split()
    cost = int(cost)
    if pre in info:
        info[pre].addDiscipline(post, cost)
    else:
        info[pre] = Node(post, cost)

q = int(input())
for _ in range(q):
    pre, post = input().split()
    tmp = {pre:0}
    queue = []
    heappush(queue, [0, pre])
    while queue:
        cost, pre = heappop(queue)
        if pre==post:
            break
        if pre in info:
            for Next, Cost in info[pre].next:
                if Next not in tmp:
                    tmp[Next] = 2**31-1
                Cost += cost
                if tmp[Next] > Cost:
                    tmp[Next] = Cost
                    heappush(queue, [Cost, Next])
    if post not in tmp or tmp[post]==2**31-1:
        tmp[post] = -1
    print(tmp[post])

input =
2 4
ox oo 4
ox xo 4
xx ox 1
xo oo 3
3
xo oo
oo xx
xx oo
result =
3
-1
5

input =
3 9
xoo oox 4
ooo xox 4
oxx xoo 5
oox ooo 3
ooo xxo 3
xox xoo 3
oxo xoo 4
ooo oox 4
ooo oxx 5
3
oxo oox
ooo oox
xxx xox
result =
8
4
-1

input =
3 6
xxx xxo 4
oxo ooo 5
xoo oox 5
xxo xox 2
xoo oxo 4
oxo xxo 1
4
xox xoo
oox xxo
oxx oxx
xoo ooo
result =
-1
-1
0
9