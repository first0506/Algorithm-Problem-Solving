# T = int(input())
# for test_case in range(1, T+1):
#     N, M, L = map(int, input().split())
#     nums = list(map(int, input().split()))
#     for _ in range(M):
#         c = input().split()
#         if c[0]=='I':
#             a, b = int(c[1]), int(c[2])
#             nums[a:a] = [b]
#             N += 1
#         elif c[0]=='D':
#             nums.pop(int(c[1]))
#             N -= 1
#         else:
#             nums[int(c[1])] = int(c[2])
#     if L >= N:
#         print('#{} -1'.format(test_case))
#     else:
#         print('#{} {}'.format(test_case, nums[L]))

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def addLast(data):
    global pHead
    if pHead==None:
        pHead = Node(data)
    else:
        pTmp = pHead
        while pTmp.next!=None:
            pTmp = pTmp.next
        pTmp.next = Node(data)

def add(idx, data):
    global pHead
    pTmp = pHead
    for _ in range(idx-1):
        pTmp = pTmp.next
    pTmp.next = Node(data, pTmp.next)

def delete(idx):
    global pHead
    pTmp = pHead
    if not idx:
        pHead = pTmp.next
    else:
        for _ in range(idx-1):
            pTmp = pTmp.next
        pTmp.next = pTmp.next.next

def replace(idx, data):
    global pHead
    pTmp = pHead
    for _ in range(idx):
        pTmp = pTmp.next
    pTmp.data = data

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    pHead = None
    ans = 0
    for i in nums:
        addLast(i)
    for _ in range(M):
        c = input().split()
        a = c[0]
        if a=='I':
            add(int(c[1]), int(c[2]))
        elif a=='D':
            delete(int(c[1]))
        else:
            replace(int(c[1]), int(c[2]))
    cnt = 0
    pTmp = pHead
    while pTmp!=None:
        if cnt==L:
            ans = pTmp.data
            break
        else:
            cnt += 1
            pTmp = pTmp.next
    if cnt < L:
        ans = -1
    print('#{} {}'.format(test_case, ans))