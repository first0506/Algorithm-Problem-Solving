def solution(relation):
    answer = []
    N = len(relation)
    M = len(relation[0])
    def combi(start, length, tmp):
        nonlocal N, M, answer
        if len(tmp)==length:
            for i in answer:
                if len(set(i+tmp))==len(tmp):
                    break
            else:
                tmp2 = []
                for k in range(N):
                    tmp1 = ''
                    for p in tmp:
                        tmp1 += relation[k][p]
                    if tmp1 in tmp2:
                        break
                    else:
                        tmp2.append(tmp1)
                else:
                    answer.append(tmp[:])
        else:
            for i in range(start, M-length+len(tmp)+1):
                tmp.append(i)
                combi(i+1, length, tmp)
                tmp.pop()
    for m in range(1, M+1):
        combi(0, m, [])
    return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# result = 2

print(solution(relation))