def solution(words, queries):   # 시간초과 3개
    answer = []
    word_dict = {}

    for i in words:
        if len(i) in word_dict:
            word_dict[len(i)].append(i)
        else:
            word_dict[len(i)] = [i]

    for q in queries:
        if len(q) in word_dict:
            cnt = 0
            for word in word_dict[len(q)]:
                for i in range(len(q)):
                    if q[i]!='?' and q[i]!=word[i]:
                        break
                else:
                    cnt += 1
            answer.append(cnt)
        else:
            answer.append(0)

    return answer

def solution(words, queries):   # 통과
    from collections import deque
    class Node:                                 # 한글자씩 노드로 저장(Trie 구조)
        def __init__(self, key, end=False):
            self.key = key                      # 한 글자
            self.end = end                      # 해당 노드가 단어의 끝 노드인지
            self.children = {}                  # 자식 노드들을 저장
            self.subcnt = 0                     # 해당 노드에 속한 단어의 수
    class Trie:
        def __init__(self):
            self.startnodes = {}                # 단어들 정방향일 때 시작노드를 단어의 길이별로 저장
            self.reverse_startnodes = {}        # 단어들 역방향일 때 시작노드를 단어의 길이별로 저장

        def insert(self, string):
            if not len(string) in self.startnodes:              # 입력 단어의 길이를 가진 Trie구조가 없을 때
                self.startnodes[len(string)] = Node(None)       # 시작노드 생성
            if not len(string) in self.reverse_startnodes:
                self.reverse_startnodes[len(string)] = Node(None)
            cur_node = self.startnodes[len(string)]             # 시작노드를 현재 노드로 저장
            reverse_cur_node = self.reverse_startnodes[len(string)]
            cur_node.subcnt += 1                                # subcnt 1씩 증가
            reverse_cur_node.subcnt += 1
            for i in range(len(string)):
                char = string[i]                                # 한 글자씩
                reverse_char = string[-i-1]
                if char not in cur_node.children:
                    cur_node.children[char] = Node(char)        # 자식노드에 없으면 생성
                if reverse_char not in reverse_cur_node.children:
                    reverse_cur_node.children[reverse_char] = Node(reverse_char)
                cur_node = cur_node.children[char]              # 현재 노드를 다음 자식 노드로 저장
                reverse_cur_node = reverse_cur_node.children[reverse_char]
                cur_node.subcnt += 1
                reverse_cur_node.subcnt += 1
            cur_node.end = True     # 마지막 글자일 때 end True
            reverse_cur_node.end = True

        def search(self, query):
            if query[0]!='?':       # 접미사일 때
                if not len(query) in self.startnodes:   # 찾는 query의 길이를 가진 단어가 없으면 0 반환
                    return 0
                cur_node = self.startnodes[len(query)]
                q = deque([(cur_node, -1)])     # bfs - (현재 노드, query의 인덱스)
                cnt = 0
                while q:
                    nod, idx = q.popleft()
                    idx += 1
                    if query[idx]=='?':     # ? 만났을 때 해당 글자 노드의 subcnt 더함
                        cnt += nod.subcnt
                    else:
                        for child in nod.children:
                            if query[idx]==child:   # query와 노드가 일치할 때 다음 노드로 진행
                                q.append((nod.children[child], idx))
            else:
                query = query[::-1]     # 접두사일 때
                if not len(query) in self.reverse_startnodes:
                    return 0
                cur_node = self.reverse_startnodes[len(query)]
                q = deque([(cur_node, -1)])
                cnt = 0
                while q:
                    nod, idx = q.popleft()
                    idx += 1
                    if query[idx]=='?':
                        cnt += nod.subcnt
                    else:
                        for child in nod.children:
                            if query[idx]==child:
                                q.append((nod.children[child], idx))
            return cnt
    answer = []
    trie = Trie()
    for word in words:
        trie.insert(word)   # words Trie에 입력
    for query in queries:
        answer.append(trie.search(query))   # query 찾은 결과 answer에 저장
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# result = [3, 2, 4, 1, 0]

print(solution(words, queries))