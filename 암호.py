class Node:
    def __init__(self, data, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next

def addLast(data):
    global pHead, pTail
    if pHead==None:
        pTail = pHead = Node(data)
    else:
        pTail.next = Node(data, pTail)
        pTail = pTail.next

def add(idx):
    global pHead, pTail
    pTmp = pHead
    for _ in range(idx-1):
        pTmp = pTmp.next
    if pTmp.next==None:
        a = pTmp.data + pHead.data
    else:
        a = pTmp.data + pTmp.next.data
    pTmp.next = Node(a, pTmp, pTmp.next)
    pTmp = pTmp.next
    if pTmp.next!=None:
        pTmp.next.pre = pTmp
    else:
        pTail = pTmp

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    pHead, pTail = None, None
    for i in nums:
        addLast(i)
    cur = 0
    for _ in range(K):
        N += 1
        cur = (cur+M)%N
        add(cur)
        if cur+M > N:
            cur += 1
    p = pTail
    cnt = 0
    ans = []
    while p!=None:
        cnt += 1
        ans.append(p.data)
        if cnt==10:
            break
        p = p.pre
    print('#{} {}'.format(test_case, ' '.join( str(i) for i in ans)))

# T = int(input())
# for test_case in range(1, T+1):
#     N, M, K = list(map(int, input().split()))
#     numbers = list(map(int, input().split()))
#     point = 0
#     for _ in range(K):
#         point = (point + M) % (len(numbers) + 1)
#         if point == len(numbers):
#             a = numbers[point - 1] + numbers[0]
#         else:
#             a = numbers[point - 1] + numbers[point]
#         numbers.insert(point, a)
#         if point + M > len(numbers):
#             point += 1
#         print(numbers)
#     result = []
#     if len(numbers) >= 10:
#         for i in range(-1, -11, -1):
#             result.append(str(numbers[i]))
#     else:
#         for i in range(-1, -len(numbers)-1, -1):
#             result.append(str(numbers[i]))
#     print('#{} {}'.format(test_case, ' '.join(result)))