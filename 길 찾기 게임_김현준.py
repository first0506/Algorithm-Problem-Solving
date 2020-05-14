def solution(nodeinfo):
    from sys import setrecursionlimit
    setrecursionlimit(10000000)
    answer = []
    nodeinfo = [[idx+1]+value for idx, value in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x:(-x[2], x[1]))
    class node:
        def __init__(self, id, x, y, left=None, right=None):
            self.id = id
            self.x = x
            self.y = y
            self.left = left
            self.right = right
    head = node(nodeinfo[0][0], nodeinfo[0][1], nodeinfo[0][2])

    def addnode(nod, wholelist):
        leftlist, rightlist = [], []
        for i in wholelist:
            if i[2] < nod.y:
                if i[1] < nod.x:
                    leftlist.append(i)
                else:
                    rightlist.append(i)
        if leftlist:
            nod.left = node(leftlist[0][0], leftlist[0][1], leftlist[0][2])
            addnode(nod.left, leftlist[1:])
        if rightlist:
            nod.right = node(rightlist[0][0], rightlist[0][1], rightlist[0][2])
            addnode(nod.right, rightlist[1:])

    def preorder(node):
        nonlocal pre_result
        pre_result.append(node.id)
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)

    def postorder(node):
        nonlocal post_result
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)
        post_result.append(node.id)

    addnode(head, nodeinfo[1:])
    pre_result = []
    post_result = []
    preorder(head)
    postorder(head)
    answer.append(pre_result)
    answer.append(post_result)

    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
# result = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

print(solution(nodeinfo))

# def solution(N, road, K):
#     answer = 0
#     towns = [0]*(N+1)
#     towns[1] = 1
#     board = [[0]*(N+1) for _ in range(N+1)]
#     for i in road:
#         if not board[i[0]][i[1]] or board[i[0]][i[1]]>i[2]:
#             board[i[0]][i[1]] = i[2]
#             board[i[1]][i[0]] = i[2]
#     q = [[1, 0]]
#     while q:
#         start, time = q.pop(0)
#         for i in range(1, N+1):
#             if board[start][i] and time+board[start][i] <=K and (not towns[i] or towns[i]>time+board[start][i]):
#                 towns[i] = time+board[start][i]
#                 q.append([i, time+board[start][i]])
#     for i in towns:
#         if i:
#             answer += 1
#     return answer
#
# N = 5
# road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
# K = 3
#
# # N = 6
# # road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
# # K = 4
#
# print(solution(N, road, K))