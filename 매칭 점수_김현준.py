def solution(word, pages):
    answer = 0
    pages_dic = {}  # 웹페이지 정보 페이지이름: [인덱스, 기본점수, 외부링크 리스트, 기본점수/외부링크수, 매칭점수]
    for idx in range(len(pages)):
        page = pages[idx]
        name = page.split('<meta property="og:url" content="https://')[-1].split('"')[0]    # 페이지이름 찾기
        links = page.split('<a href="https://')
        link = []
        for i in range(1, len(links)):
            link.append(links[i].split('"')[0]) # 외부 링크 찾기
        body = page.split('<body>')[-1].split('</body>')[0].split('\n') # body 부분만 떼고 줄바꿈 없애기
        basic = 0   # 기본점수
        word = word.lower() # 찾을 문자 소문자화
        for i in range(len(body)):
            if '</a>' in body[i]:   # body 내 외부링크가 있는 줄 검색단어 개수 찾기
                body1 = body[i].split('<')
                for j in body1:
                    if '>' in j:
                        basic += find(word, j.split('>')[-1])
                    else:
                        basic += find(word,j)
            else:
                basic += find(word, body[i])    # 외부링크 없는 줄 검색단어 개수 찾기
        if not link:    # 외부링크가 없으면 기본점수/외부링크 수 = 0
            linkscore = 0
        else:
            linkscore = basic/len(link) # 외부링크 있으면
        pages_dic[name] = [idx, basic, link, linkscore, basic]  # 페이지 정보 저장 (매칭점수를 기본점수로 시작)
    for page in pages_dic.keys():
        for link in pages_dic[page][2]: # 페이지의 외부링크 탐색
            if link in pages_dic:   # 외부링크가 딕셔너리에 있으면
                pages_dic[link][4] += pages_dic[page][3]    # 매칭점수에 추가
    maxscore = 0
    for i in pages_dic.values():    # 최대 매칭점수의 인덱스 찾기
        if i[4] > maxscore:
            answer = i[0]
            maxscore = i[4]
    return answer

def find(word, words):  # 단어구문 내 검색단어 찾기
    if not words or len(word)>len(words):   # 빈칸이거나 검색단어보다 짧으면 return 0
        return 0
    result = 0
    words = ' '+words.lower()+' '   # 단어구문 모두 소문자화하고 양 옆에 빈칸 추가(인덱스 편이를 위해)
    for i in range(1, len(words)-len(word)):
        if words[i:i+len(word)]==word and not words[i-1].isalpha() and not words[i+len(word)].isalpha():
            result += 1     # 검색단어가 단어구문 내 존재하고 검색단어 앞 뒤에 알파벳이 아니면 result 증가
    return result


word = 'blind'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
#result = 0

# word = 'Muzi'
# pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
# #result = 1

print(solution(word, pages))