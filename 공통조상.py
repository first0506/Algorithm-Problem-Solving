class Node():
    def __init__(self):
        self.parent = 0
        self.child = []

def findParent(i):
    tmp = v[i]
    parents = [i]
    while tmp.parent:
        parents.append(tmp.parent)
        tmp = v[tmp.parent]
    return parents

def countChild(i):
    global ans
    ans += 1
    for c in v[i].child:
        countChild(c)

T = int(input())
for test_case in range(1, T+1):
    V, E, a, b = map(int, input().split())
    nodes = list(map(int, input().split()))
    v = [Node() for _ in range(V+1)]
    for i in range(E):
        s, e = nodes[2*i], nodes[2*i+1]
        v[s].child.append(e)
        v[e].parent = s
    aParents = findParent(a)
    bParents = findParent(b)
    p = 0
    for i in range(-1, -min(len(aParents), len(bParents))-1, -1):
        if aParents[i]!=bParents[i]:
            p = aParents[i+1]
            break
    ans = 0
    countChild(p)
    print('#{} {} {}'.format(test_case, p, ans))