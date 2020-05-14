def solution(dataSource, tags):
    answer = []
    group = {}
    for doc in dataSource:
        for i in range(1, len(doc)):
            if doc[i] not in group:
                group[doc[i]] = [doc[0]]
            else:
                group[doc[i]].append(doc[0])
    result = []
    for tag in tags:
        result += group[tag]
    result1 = list(set(result))
    result2 = []
    for i in result1:
        result2.append([i, result.count(i)])
    result3 = sorted(result2, key=lambda x : (-x[1], x[0]))[:10]
    for i in result3:
        answer.append(i[0])
    return answer
dataSource =[
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]
tags = ["t1", "t2", "t3"]
print(solution(dataSource, tags))