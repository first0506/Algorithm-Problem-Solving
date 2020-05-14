# T = int(input())
# for test_case in range(1, T+1):
#     N, M, L = map(int, input().split())
#     nums = list(map(int, input().split()))
#     for _ in range(M):
#         a, b = map(int, input().split())
#         nums[a:a] = b
#     print('#{} {}'.format(test_case, nums[L]))

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
        while pTmp.next!=None: # 마지막 노드가 아니면
            pTmp = pTmp.next
        pTmp.next = Node(data) # 이전의 마지막노드에 새 노드 주소 저장

def add(idx, data):
    global pHead
    pTmp = pHead
    if pTmp == None: # 노드가 없는 경우 idx는 0만 입력됨
        pHead = Node(data)
    else:
        for i in range(idx-1): # pTmp는 idx의 앞 노드 주소
            pTmp = pTmp.next    # 다음 노드 지정
        p = Node(data, pTmp.next)   # idx노드의 다음 노드 주소를 새 노드에 저장
        pTmp.next = p               # idx 앞 노드에 새 노드 주소 저장

T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    pHead = None
    for i in nums:
        addLast(i)
    for _ in range(M):
        a, b = map(int, input().split())
        add(a, b)
    p = pHead
    for _ in range(L):
        p = p.next
    print('#{} {}'.format(test_case, p.data))