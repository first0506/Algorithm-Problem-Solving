# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     for i in range(M):
#         if not i:
#             result = list(map(int, input().split()))
#         else:
#             tmp = list(map(int, input().split()))
#             for k in range(len(result)):
#                 if result[k] > tmp[0]:
#                     result[k:k] = tmp
#                     break
#             else:
#                 result = result+tmp
#     print('#{} {}'.format(test_case, ' '.join(str(i) for i in result[-1:-11:-1])))

class Node:
    def __init__(self, data, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next

def addLast(data):
    global pHead, pTail
    if pHead==None:
        pHead = pTail = Node(data)
    else:
        pTmp = pHead
        while pTmp.next!=None:
            pTmp = pTmp.next
        pTmp.next = Node(data, pTmp)
        pTail = pTmp.next

def add(pTmp, data):
    global pHead
    if pTmp.pre==None:
        pTmp.pre = Node(data, None, pTmp)
        pHead = pTmp.pre
    else:
        pTmp.pre = Node(data, pTmp.pre, pTmp)
        pTmp = pTmp.pre
        pTmp.pre.next = pTmp

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    pHead, pTail = None, None
    nums = list(map(int, input().split()))
    for i in nums:
        addLast(i)
    for _ in range(M-1):
        a = list(map(int, input().split()))
        pTmp = pHead
        while pTmp!=None:
            if pTmp.data > a[0]:
                for i in a:
                    add(pTmp, i)
                break
            pTmp = pTmp.next
        if pTmp==None:
            for i in a:
                addLast(i)
    ans = []
    p = pTail
    for _ in range(10):
        ans.append(p.data)
        p = p.pre
    print('#{} {}'.format(test_case, ' '.join(str(i) for i in ans)))