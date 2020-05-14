def solution(words):
    answer = 0
    words.sort()    # 단어들 사전 순으로 정렬
    for i in range(len(words)):
        word = words[i] # word = 현재 탐색하는 단어
        p, n = False, False # p = word 왼쪽 단어 조건 충족 여부, n = word 오른쪽 단어 조건 충족 여부
        if i!=0:    # word가 첫번째 단어가 아니면
            pre = words[i-1]    # pre = word 왼쪽 단어
        else:
            p = True    # 첫번쨰 단어면 왼쪽 단어 비교 안해도 되므로 True
        if i!=len(words)-1: # word가 마지막 단어가 아니면
            next = words[i+1]   # next = word 오른쪽 단어
        else:
            n = True    # 마지막 단어면 오른쪽 단어 비교 안해도 되므로 True
        for k in range(len(word)):  # 앞에서부터 한 철자씩 비교    (몇 번째 글자인지 -> 최소 k를 찾아야한다)
            if not p and len(pre) <= k: # k가 pre단어 길이보다 길 때 비교 안해도 되므로 True
                p = True
            if not n and len(next) <= k:
                n = True
            if not p:
                if pre[k]!=word[k]: # pre와 철자가 달라졌다면
                    p = True
            if not n:
                if next[k]!=word[k]:    # next와 철자가 달라졌다면
                    n = True
            if p and n: # 왼쪽, 오른쪽 모두 비교 완료되면
                break
        answer += k+1   # 인덱스 0부터 시작이므로 +1
    return answer

words = ['go','gone','guild'] # 7
# words = ['abc','def','ghi','jklm'] # 4
# words = ['word','war','warrior','world'] # 15

print(solution(words))